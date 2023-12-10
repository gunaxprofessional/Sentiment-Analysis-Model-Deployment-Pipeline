from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import mysql.connector

app = Flask(__name__)

# Replace these with your actual database credentials
DB_HOST = "ecommerce.ch0s2ra5njdh.us-east-2.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_NAME = "ecommerce"

# Establish a connection to the database


def create_connection():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection


# Load the model and tokenizer
loaded_model = load_model('sentiment_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        sentence = request.form['sentence']
        prediction = predict_sentiment(sentence)

        # Log prediction to MySQL database
        log_prediction(sentence, prediction)

        return render_template('index.html', sentence=sentence, prediction=prediction)


def predict_sentiment(sentence):
    # Tokenize and pad the input sentence
    sequence = loaded_tokenizer.texts_to_sequences([sentence])
    padded_sequence = pad_sequences(
        sequence, maxlen=200, padding='post', truncating='post')

    # Make the prediction
    result = loaded_model.predict(padded_sequence)

    # Interpret the prediction
    if result[0][0] > 0.5:
        return "Positive"
    else:
        return "Negative"


def log_prediction(sentence, prediction):
    connection = create_connection()
    cursor = connection.cursor()

    # Check if the table exists; create it if not
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS predictions (id INT AUTO_INCREMENT PRIMARY KEY, sentence TEXT, prediction TEXT)")

    # Insert the prediction into the table
    cursor.execute(
        "INSERT INTO predictions (sentence, prediction) VALUES (%s, %s)", (sentence, prediction))

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    app.run(debug=True, port=5002)
