pipeline {
    agent any

    environment {
        DEPENDENCY_CHECK_REPORT = 'dependency-check-report.html'
        BANDIT_REPORT = 'bandit-report.html'
        ZAP_HOME = '/path/to/zap' // Update with the actual path to ZAP
        ZAP_REPORT = 'zap-report.html'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/ramsecinfo/Python-Sample.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip install -r requirements.txt'
                    sh 'pip install bandit'
                    sh 'pip install safety'
                }
            }
        }
environment {
        DEPENDENCY_CHECK_HOME = '/path/to/dependency-check'
        PATH = "${DEPENDENCY_CHECK_HOME}:${env.PATH}"
        DEPENDENCY_CHECK_REPORT = 'dependency-check-report.html'
        BANDIT_REPORT = 'bandit-report.html'
        ZAP_HOME = '/path/to/zap' // Update with the actual path to ZAP
        ZAP_REPORT = 'zap-report.html'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your/repository.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip install -r requirements.txt'
                    sh 'pip install bandit'
                    sh 'pip install safety'
                }
            }
       pipeline {
    agent any

    environment {
        DEPENDENCY_CHECK_REPORT = 'dependency-check-report/dependency-check-report.html'
        BANDIT_REPORT = 'bandit-report.html'
        ZAP_REPORT = 'zap-report.html'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your/repository.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip install -r requirements.txt'
                    sh 'pip install bandit'
                    sh 'pip install safety'
                }
            }
        }

        stage('Static Code Analysis (SCA)') {
            steps {
                script {
                    echo 'Running OWASP Dependency-Check using Docker...'
                    sh '''
                    docker run --rm -v $(pwd):/src -v $(pwd)/dependency-check-report:/report owasp/dependency-check \
                    --project "YourProject" --scan /src --format HTML --out /report
                    '''
                }
                publishHTML(target: [
                    reportName: 'Dependency-Check Report',
                    reportDir: 'dependency-check-report',
                    reportFiles: 'dependency-check-report.html',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                ])
            }
        }

        stage('Static Application Security Testing (SAST)') {
            steps {
                script {
                    echo 'Running Bandit...'
                    sh 'bandit -r . -f html -o ${BANDIT_REPORT}'
                }
                publishHTML(target: [
                    reportName: 'Bandit Report',
                    reportDir: '.',
                    reportFiles: BANDIT_REPORT,
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                ])
            }
        }

        stage('Build Application') {
            steps {
                script {
                    echo 'Building the application...'
                    sh 'python setup.py build'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    echo 'Deploying the application...'
                    // Add your deployment steps here
                }
            }
        }

        stage('Dynamic Application Security Testing (DAST)') {
            steps {
                script {
                    echo 'Running OWASP ZAP...'
                    sh "docker run -d --name zap -u zap -p 8080:8080 owasp/zap2docker-stable zap.sh -daemon -port 8080 -config api.disablekey=true"
                    sleep 30 // Give ZAP time to start

                    echo 'Scanning the application...'
                    sh "curl 'http://localhost:8080/JSON/ascan/action/scan/?url=http://your-application-url'"

                    sleep 300 // Adjust sleep duration based on scan size

                    echo 'Generating ZAP report...'
                    sh "curl 'http://localhost:8080/OTHER/core/other/htmlreport/?' -o ${ZAP_REPORT}"

                    echo 'Stopping ZAP...'
                    sh "docker stop zap && docker rm zap"
                }
                publishHTML(target: [
                    reportName: 'OWASP ZAP Report',
                    reportDir: '.',
                    reportFiles: ZAP_REPORT,
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                ])
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

         
