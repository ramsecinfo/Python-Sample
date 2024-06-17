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
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t username/docker-image-name .'
                }
            }
        }
 environment {
        DOCKER_CREDENTIALS_ID = 'your-docker-credentials-id'
    }
    stages {
        stage('Build and Push') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS_ID) {
                        def image = docker.build('rupokify/python-jenkins-testone:latest')
                        image.push()
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
