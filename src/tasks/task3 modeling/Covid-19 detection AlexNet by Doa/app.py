import streamlit as st
from PIL import Image

st.title("Detecting Covid-19 Cases")
#st.header("Covid 19 Detection")
cover_image = Image.open("covid19-image.png")
st.image(cover_image, use_column_width=True)
st.header("Upload CT image to check if it is positive or negative Covid-19 ")

from img_classification import Model_predict
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)


uploaded_file = st.file_uploader("select Image ...")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded CT Photo', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = Model_predict(image)
    #st.write(label)
    

    if label == 'CT_COVID':
        #st.write("Case is Positive")
        st.markdown('<p class="big-font">Case is Positive</p>', unsafe_allow_html=True)

        
    else:
        #st.write("Case is Negative")
        st.markdown('<p class="big-font">Case is Negative</p>', unsafe_allow_html=True)





