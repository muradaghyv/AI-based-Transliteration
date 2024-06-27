import streamlit as st
import cv2
import numpy as np

st.title("Uploading an image")

if "img" in st.session_state:
    st.info("Image was already uploaded!")
    new_file = st.file_uploader("Upload a new image", type=["jpg", "png", "jpeg"])
    if new_file is not None:
        file_bytes = np.asarray(bytearray(new_file.read()), dtype=np.uint8)
        new_image = cv2.imdecode(file_bytes, 1)
        st.session_state["img"] = new_image
        st.image(image=st.session_state["img"], caption="New image", use_column_width=True)
        st.info("New image uploaded successfully!")
    
else:
    uploaded_file = st.file_uploader("Upload image", type = ["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # image = cv2.imread(uploaded_file)
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        st.session_state["img"] = image
        st.image(image=st.session_state["img"], caption="Uploaded image", use_column_width=True)
        st.write("The image uploaded succesfully!")
        