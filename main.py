"""This module runs a Flask app"""
from flask import Flask, render_template, request
# from PIL import Image
# import numpy as np
# from keras.preprocessing.image import load_img, img_to_array
# from keras.applications.vgg16 import preprocess_input, decode_predictions
# # from keras.applications.vgg16 import VGG16
# import tensorflow as tf

# model = tf.keras.applications.vgg16.VGG16(
#     include_top=True,
#     weights='imagenet',
#     input_tensor=None,
#     input_shape=None,
#     pooling=None,
#     classes=1000,
#     classifier_activation='softmax'
# )

app = Flask('img_classifier')
# Load the VGG16 model with pre-trained weights
# model = VGG16(weights='imagenet')

@app.route('/')
"""this function renders inputted images"""
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
"""this function predicts what that inputted images is"""
def predict():
    imagefile = request.files['imagefile']
    # ------- saving the image somewhere locally -----
    # save the input image now
    image_path = 'images/' + imagefile.filename
    print('image path', image_path)
    imagefile.save(image_path)
    #   img = load_img(image_path, target_size=(224, 224))  # Resize image to VGG16 input shape
    #   img_array = img_to_array(img)
    #   print('img shape', img_array.shape) # (224, 224, 3)
    #   img_array = np.expand_dims(img_array, axis=0)  # Add a batch dimension (1, 224, 224, 3)
    #   img_array = preprocess_input(img_array)
    #   # Make predictions using the loaded model
    #   predictions = model.predict(img_array)
    #   decoded_predictions = decode_predictions(predictions, top=3)[0]  # Get top 3 predictions
    #   print(decoded_predictions)
    # Convert the prediction results to a list of tuples (label, description, probability)
    # results = [(label, description, probability) 
    #   for (label, description, probability) in decoded_predictions]
    #   print(results)

    return render_template('index.html')

app.run(host='0.0.0.0', port=5001)
