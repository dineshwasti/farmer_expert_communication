# classifier/classify.py
import os
from PIL import Image

from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from keras.applications.mobilenet_v2 import MobileNetV2
import numpy as np
from keras.models import load_model
from keras.utils import load_img,img_to_array
model_path = './models/final_nas.h5'  # Update with the path to your custom model
model = load_model(model_path)

def classify_image(image_path):
    #model_path = './models/eden.h5'  # Update with the path to your custom model
    
    #model = load_model(model_path)

    
    class_labels = ['Green Mold','Healthy Mushroom','Healthy Mycelium','Yellow Blotch']

    
    img = Image.open(image_path).convert('RGB')
    img = img.resize((224,224))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    predictions = model.predict(x)

    predicted_label_index = np.argmax(predictions[0])
    predicted_label = class_labels[predicted_label_index]
    print(predicted_label)
    prediction_probs = model.predict(np.expand_dims(img, axis=0))
    print(prediction_probs)


    return predicted_label,prediction_probs
    








