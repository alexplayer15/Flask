pipeline {
    agent any

    // environment {
    //     DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials') 
    // }

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
            // print version of python so we can check we have the same versions
            sh 'python3 --version'
            
            // update python package manager
            sh 'python3 -m pip install --upgrade pip'            

            // Example: Install Python dependencies using pip
            sh 'python3 -m pip install -r dependencies.txt'
            
            // Example: Run linting
            sh 'python3 -m pylint main.py'
                
            // Set up the virtual environment
            sh '''
                python3 -m venv test
                . test/bin/activate
             '''
            
        }
    }

    stage('Test') {
        steps {
            sh 'python3 -m pip list'
             // Activate the virtual environment and run tests
            sh '. test/bin/activate && python3 -m pip install -r dependencies.txt && python3 -m pytest tests.py'
            sh 'exit' // Deactivate the virtual environment after tests
     }
    }

    stage('Deploy to Docker'){
        steps {
            script {
                // withDockerRegistry([credentialsId: 'docker-hub-credentials', url:'https://index.docker.io/v1/'])
                     sh 'docker buildx build -t alexplayer15/flask-app .'                    
                     // sh "docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}"
                     // sh 'docker push alexplayer15/flask-app'
                     // sh 'docker rm -f flask-container || true'
                     sh 'docker container run -d -p 5001:5001 --name flask-container alexplayer15/flask-app'
            }
        }
    }
}
}
                




