pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                script {
                    git credentialsId: 'mmtnc', url: 'https://github.com/hoangtukbl/mmtnc.git'
                }
            }
        }

        stage('Build and publish Docker Image') {
            steps {
                script{
                    withDockerRegistry(credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/') 
                        sh 'docker build -t realanhtu812/21127466'
                        sh 'docker push realanhtu812/21127466'
                }
            }
        }

    }
}

