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
            // Example: Install Python dependencies using pip
            sh 'pip install -r requirements.txt'
            
            // Example: Run linting
            sh 'pylint your_code.py'
            
            // Example: Run unit tests
            sh 'python -m unittest discover -s tests -p "*_test.py"'
    }
}
    from flask import Flask, render_template, request
    from PIL import Image
    import numpy as np
    from keras.preprocessing.image import load_img, img_to_array
    from keras.applications.vgg16 import preprocess_input, decode_predictions
    # from keras.applications.vgg16 import VGG16
    import tensorflow as tf
    }
}
