pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }

    environment {
        SCAN_REPORT_DIR = "${env.WORKSPACE}/scan-reports"
        SCA_TOOL = 'safety'
        SAST_TOOL = 'bandit'
        DAST_TOOL = 'owasp/zap2docker-stable'
        SAFETY_CONFIG_DIR = "${env.WORKSPACE}/.safety" // Add this line
    }

    stages {
        stage('Prepare') {
            steps {
                script {
                    // Ensure the scan report directory exists
                    sh "mkdir -p ${SCAN_REPORT_DIR}"
                    // Ensure the safety config directory exists
                    sh "mkdir -p ${SAFETY_CONFIG_DIR}"
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python -m venv venv'
                    // Activate the virtual environment and install dependencies
                    sh './venv/bin/pip install -r requirements.txt'
                    // Install SCA tool in the virtual environment
                    sh "./venv/bin/pip install ${SCA_TOOL}"
                    // Install SAST tool in the virtual environment
                    sh "./venv/bin/pip install ${SAST_TOOL}"
                }
            }
        }

        stage('SCA - Software Composition Analysis') {
            steps {
                script {
                    // Run safety check for known vulnerabilities in dependencies
                    sh "./venv/bin/${SCA_TOOL} check -r requirements.txt --json > ${SCAN_REPORT_DIR}/safety_report.json"
                }
            }
        }

        stage('SAST - Static Application Security Testing') {
            steps {
                script {
                    // Ensure the scan report directory exists
                    sh "mkdir -p ${SCAN_REPORT_DIR}"
                    
                    // Run bandit to find common security issues in Python code
                    sh "./venv/bin/${SAST_TOOL} -r . -f json -o ${SCAN_REPORT_DIR}/bandit_report.json || true"
                }
            }
        }

        stage('DAST - Dynamic Application Security Testing') {
            steps {
                script {
                    // Ensure the application is running and accessible
                    // This example assumes a script is available to start the application
                    sh './start_application.sh'

                    // Run OWASP ZAP for dynamic application security testing
                    sh """
                        docker run -t --rm -v ${SCAN_REPORT_DIR}:/zap/wrk/:rw \
                        -u zap ${DAST_TOOL} zap-baseline.py \
                        -t http://localhost:8000 \
                        -r /zap/wrk/zap_report.html
                    """
                }
            }
        }
        
        stage('Archive Reports') {
            steps {
                script {
                    // Archive the security scan reports
                    archiveArtifacts artifacts: 'scan-reports/*', allowEmptyArchive: true
                }
            }
        }
    }

    post {
        always {
            // Clean up the workspace
            cleanWs()
        }
    }
}
