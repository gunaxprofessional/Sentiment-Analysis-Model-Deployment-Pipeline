# Sentiment Analysis Model Deployment Pipeline

This project demonstrates the deployment of a sentiment analysis model using LSTM, a web service, and a deployment pipeline with Docker and Kubernetes. The sentiment analysis model is built using TensorFlow, and the web service is implemented in Python with Flask. The MySQL database is hosted on AWS RDS. Below is a comprehensive guide on setting up and running the entire system.

# Demo:
![image](https://github.com/gunaxprofessional/Sentiment-Analysis-Model-Deployment-Pipeline/assets/66107066/f1f3cc54-a910-4197-a8d1-1219c51af1f8)


## Table of Contents

1. [AI Model Development](#ai-model-development)
2. [Web Service Creation](#web-service-creation)
3. [MySQL Database Interaction](#mysql-database-interaction)
4. [Containerization with Docker](#containerization-with-docker)
5. [Deployment with Kubernetes](#deployment-with-kubernetes)
6. [Documentation](#documentation)
7. [Bonus Features](#bonus-features)

## AI Model Development

The sentiment analysis model is developed using LSTM, achieving an accuracy of 87%. Python is used as the programming language, and TensorFlow serves as the machine learning framework.

**Note:** To obtain the model pickle file (sentiment_model.h5), run the notebook.ipynb provided in the repository.



## Web Service Creation

A web service is implemented in Python using Flask to serve the sentiment analysis model. The service exposes an API endpoint allowing users to submit text snippets and receive model predictions. The service logs prediction requests and results in a MySQL database hosted on AWS RDS.

## MySQL Database Interaction

For MySQL database interaction, the user needs to enter the following details:

- Host
- User
- Password
- Database Name

Use the `sql.py` Python file to retrieve information from the database.


## Containerization with Docker

The AI model and the web service are containerized using Docker. The Dockerfile specifies the environment, dependencies, and how the application should run. The container exposes port 5002, and Gunicorn is used to run the Flask app.

## Deployment with Kubernetes

The deployment is managed using Kubernetes. The `deployment.yaml` file defines a Deployment and a Service. The Deployment ensures the desired number of replicas (pods) are running, and the Service exposes the web service externally.

## Documentation

### Setup and Execution

Follow these steps to set up and run the project:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/gunaxprofessional/Sentiment-Analysis-Model-Deployment-Pipeline.git
   cd Sentiment-Analysis-Model-Deployment-Pipeline
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Web Service Locally:**

   ```bash
   python app.py
   ```

   Access the service at [http://localhost:5002](http://localhost:5002).

4. **Build Docker Image:**

   ```bash
   docker build -t sentimentdockerimg .
   ```

5. **Run Docker Container:**

   ```bash
   docker run -p 5002:5002 sentimentdockerimg
   ```

   Access the service at [http://localhost:5002](http://localhost:5002).

6. **Kubernetes Deployment:**

   Apply the Kubernetes deployment configuration:

   ```bash
   kubectl apply -f deployment.yaml
   ```
    Start minikube:

     ```bash
     minikube start
     ```
     Monitor the deployment:
  
     ```bash
     kubectl get deployments
     kubectl get pods
     kubectl get services
     ```

   Access the service based on the external IP or NodePort provided.

### Bonus Features

- **Front-End Interface:**

  A simple front-end interface is added for user interaction. Access the interface at [http://localhost:5002](http://localhost:5002).
