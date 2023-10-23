pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Use the Git plugin to check out your repository
                script {
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/alexplayer15/Flask.git']]])
                }
            }
        }
        // Add other stages as needed
    }
}
