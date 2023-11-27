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
def hello_world():
  return render_template('index.html')

@app.route('/', methods=['POST'])
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
    # # Convert the prediction results to a list of tuples (label, description, probability)
    #   results = [(label, description, probability) for (label, description, probability) in decoded_predictions]
    #   print(results)

    return render_template('index.html')

app.run(host='0.0.0.0', port=5001)







































































# from flask import Flask, render_template, request

# app = Flask('img_classifier')

# @app.route('/')
# def hello_world():
#   return render_template('index.html')
#   # return '<h1>Hello World</h1>'

# @app.route('/', methods=['POST'])
# def predict():
#   imagefile = request.files['imagefile']
#   # ------- basically saving the image somewhere locally -----
#   # save the input image now
#   image_path = 'images/' + imagefile.filename 
#   print(image_path)
#   imagefile.save(image_path)

#   # 1.load the image in a format that keras can read

#   # 2.define our model for classification (VGG16, Resnet50)

#   # 3.pass the loaded image to the model which should output a prediction as text

#   # 4.pass that text prediction back to the webpage using flask

#   # commit this project to github (bootstrap, html, flask docs, check github for tutorial (search))
  
#   return render_template('index.html') # basic placeholder 


# app.run(host='0.0.0.0', port=1000)
