pipeline {
 
    agent any
 
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', credentialsId: 'github', url: 'https://github.com/ramsecinfo/Python-Sample.git'
            }
        }
 
        stage('Prepare') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
 
        stage('Test') {
            steps {
                sh 'pytest testRoutes.py'
            }
        }
     
 
        stage('SCA') {
            steps {
                dependencyCheck additionalArguments: '', odcInstallation: 'OWASP-Dependency-Scan'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }
 
        stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Ensure the Jenkins user has Docker permissions
                    sh 'sudo usermod -aG docker jenkins'
                    sh 'newgrp docker'
                    // Build the Docker image
                    sh 'docker build -t username/docker-image-name .'
                }
            }
        }
    }
 
         environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials' // ID of Docker Hub credentials in Jenkins
        IMAGE_NAME = 'rupokify/python-jenkins-testone'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${IMAGE_NAME} .'
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                        sh 'docker push ${IMAGE_NAME}'
                    }
                }
            }
        }
    }
 
        stage('DAST') {
            steps {
                script {
                    sh 'trivy image username/docker-image-name:latest'
                }
            }
        }
 
    }
 
}
