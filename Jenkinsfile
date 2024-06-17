pipeline {
    agent any

    environment {
        // Define the tools and environments
        SCAN_REPORT_DIR = "${WORKSPACE}/scan-reports"
        SCA_TOOL = 'safety'
        SAST_TOOL = 'bandit'
        DAST_TOOL = 'owasp/zap2docker-stable'
    }

    stages {
        stage('Prepare') {
            steps {
                script {
                    // Ensure the scan report directory exists
                    sh "mkdir -p ${SCAN_REPORT_DIR}"
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    // Install Python dependencies
                    sh 'pip install -r requirements.txt'
                    // Install SCA tool
                    sh "pip install ${SCA_TOOL}"
                    // Install SAST tool
                    sh "pip install ${SAST_TOOL}"
                }
            }
        }

        stage('SCA - Software Composition Analysis') {
            steps {
                script {
                    // Run safety check for known vulnerabilities in dependencies
                    sh "${SCA_TOOL} check -r requirements.txt --json > ${SCAN_REPORT_DIR}/safety_report.json"
                }
            }
        }

        stage('SAST - Static Application Security Testing') {
            steps {
                script {
                    // Run bandit to find common security issues in Python code
                    sh "${SAST_TOOL} -r . -f json -o ${SCAN_REPORT_DIR}/bandit_report.json"
                }
            }
        }

        stage('DAST - Dynamic Application Security Testing') {
            steps {
                script {
                    // Run OWASP ZAP for dynamic application security testing
                    // Assuming the application is already running and accessible at http://localhost:8000
                    sh "docker run -t --rm -v ${SCAN_REPORT_DIR}:/zap/wrk/:rw -u zap ${DAST_TOOL} zap-baseline.py -t http://localhost:8000 -r ${SCAN_REPORT_DIR}/zap_report.html"
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
