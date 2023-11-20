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
    stage('Build') {
        steps {
            // update python package manager
            sh 'pip3 install --upgrade pip'            

            // Example: Install Python dependencies using pip
            sh 'pip3 install -r dependencies.txt'
            
            // Example: Run linting
            sh 'pylint main.py'
            
            // Example: Run unit tests
            // sh 'python -m unittest discover -s tests -p "*_test.py"'
        }
    }

}
}
