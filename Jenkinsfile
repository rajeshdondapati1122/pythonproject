pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rocky123/pythonproject.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }

        stage('Compile Code') {
            steps {
                sh 'python -m compileall src'
            }
        }

        stage('Build Artifact') {
            steps {
                sh 'python setup.py sdist bdist_wheel'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/.whl, dist/.tar.gz', fingerprint: true
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
