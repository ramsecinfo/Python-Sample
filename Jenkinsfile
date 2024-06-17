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
 
        stage('Deploy') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dhpass', usernameVariable: 'dhuser')]) {
                        sh 'docker login -u ${dhuser} -p ${dhpass}'
                        sh 'docker push rupokify/python-jenkins-testone'
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
