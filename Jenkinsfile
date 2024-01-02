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

        stage('Build and publish Docker Image') {
            steps {
                script{
                    withDockerrRegistry(credentialsId: 'dckr_pat_d9POQMYVS737hAgiuzG_4ezUkWg', url: 'https://index.docker.io/v1/')
                        sh 'docker build -t realanhtu812/21127466'
                        sh 'docker push realanhtu812/21127466'
                }
            }
        }

        // stage('Build Docker Image') {
        //     steps {
        //         // Build Docker image
        //         script {
        //             docker.build('your-docker-image:latest', '.')
        //         }
        //     }
        // }

        // stage('Deploy to Docker') {
        //     steps {
        //         // Deploy Docker image
        //         script {
        //             docker.withRegistry('https://registry.example.com', 'your-docker-credentials-id') {
        //                 def customImage = docker.image('your-docker-image:latest')
        //                 customImage.inside {
        //                     // No specific deployment steps needed, as CMD in Dockerfile will run main.py
        //                 }
        //             }
        //         }
        //     }
        // }
    }
}
