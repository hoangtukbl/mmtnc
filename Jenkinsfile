pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                script {
                    git credentialsId: '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', url: 'https://github.com/hoangtukbl/mmtnc.git'
                }
            }
        }

        stage('Build') {
            steps {
                // Add build steps as needed
                script {
                    // Your build commands or scripts
                    sh 'echo "Building the project"'
                }
            }
        }

        stage('Test') {
            steps {
                // Add test steps as needed
                script {
                    // Your test commands or scripts
                    sh 'echo "Running tests"'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Add deployment steps as needed
                script {
                    // Your deployment commands or scripts
                    sh 'echo "Deploying the project"'
                }
            }
        }
    }
}
