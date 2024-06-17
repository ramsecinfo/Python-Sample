pipeline {
 
    agent any
 
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github', url: '<a class="vglnk" href="https://github.com/username/your-repository-name.git" rel="nofollow"><span>https</span><span>://</span><span>github</span><span>.</span><span>com</span><span>/</span><span>username</span><span>/</span><span>your</span><span>-</span><span>repository</span><span>-</span><span>name</span><span>.</span><span>git</span></a>'
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
 
        stage('SAST') {
            steps {
                sh 'safety check'
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
