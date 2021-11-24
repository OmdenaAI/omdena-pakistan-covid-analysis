# Libraries
import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from PIL import Image, ImageOps

@st.cache(allow_output_mutation=True)
def load_model():
    f = open('model.json', 'r')
    json = f.read()
    f.close()

    model = model_from_json(json)
    model.load_weights('model_weights.h5')
    return model

# Title
st.write("# COVID Patient Xray Diagnosis")

# Title image
st.image(Image.open('title.png'), use_column_width=True)

# Load model
model = load_model()

# File Uploader
file_image = st.file_uploader("Upload an X-ray image", type=["png", "jpg", "jpeg"])

if(file_image is not None):
    image = Image.open(file_image)

    if image is not None:
        image = ImageOps.fit(image, (299,299), Image.ANTIALIAS)
        image = ImageOps.grayscale(image)

        a = np.asarray(image)
        a = np.expand_dims(a, axis=0)

        pred = model.predict(a)

        col1, col2 = st.columns(2)
        col1.image(image, use_column_width=False, caption='Patients Xray Image')

        result = None
        if(pred[0] == 0):
            # COVID
            col2.image(Image.open('result_positive.png'), use_column_width=False)
        else:
            # Normal
            col2.image(Image.open('result_negative.png'), use_column_width=False)

        
        

