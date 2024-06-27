import streamlit as st
import numpy as np
import cv2

st.title("Image modification")
    
if "img_modif" or "img" in st.session_state:
    image = st.session_state["img"]
    
    emboss_kernel = np.array([[0, 0, -1],
                              [1, 0, -1],
                              [1, 1, 0]])
    emboss_img = cv2.filter2D(src=image, ddepth=-1, kernel=emboss_kernel)
    
    st.session_state["img_modif"] = emboss_img
    
    st.info("Image modified successfully!")
    
    st.image(image=image, caption="Original Image", use_column_width=True)
    st.image(image=emboss_img, caption="Modified Image", use_column_width=True)
    
    option = st.selectbox("Select options:",
                          ("Select image version for the OCR tool:", "Original Image", "Enhanced Image"))
    if option == "Original Image":
        st.session_state["final"] = image
    else:
        st.session_state["final"] = emboss_img
   
else:
    st.error("Please upload an image!")