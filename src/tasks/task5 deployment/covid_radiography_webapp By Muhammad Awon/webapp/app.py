import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps


# Title
st.title('Covid Image Classifier')
# Display image
display_img = Image.open('covid-webapp/images/display_image.jpg')
st.image(display_img, use_column_width=True)

# Create function to load model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('covid-webapp/mobilnetv3small_saved_model')
    return model

# Load model
with st.spinner('Model is being loaded...'):
    model = load_model()
# Classes
class_names = ['covid', 'normal']
# Load image file
file = st.file_uploader('Upload an X-ray image to find out if it is Covid or Normal',
                        type=['png', 'jpg', 'jpeg'])


# Create function to import image and make predictions
st.set_option('deprecation.showfileUploaderEncoding', False)
def load_and_pred_image(filename, model, img_size=(224,224)):

    img = ImageOps.fit(filename, img_size, Image.ANTIALIAS)
    img = np.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = tf.expand_dims(img, axis=0)
    
    pred = model.predict(img)
    return pred

# Make prediction score and predict class if image is available
if file is None:
    st.subheader('Please upload an image file')
else:
    img = Image.open(file)
    st.image(img)
    predictions = load_and_pred_image(img, model)
    pred_score = tf.nn.softmax(predictions[0])
    pred_class = class_names[np.argmax(pred_score)]

    pred_button = st.button('Predict')
    if pred_button:
        st.success(f"This image belongs to {pred_class} class with a {100*np.max(pred_score):.2f} percent confidence.")

