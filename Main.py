import streamlit as st

st.title("Transliteration procedure from the Cyrillic alphabet to the Latin alphabet")

st.write("""
         The transliteration project involves mainly 2 processes:
             Optical Character Recognition (OCR);
             Transliteration.
             As because we are working with images not word, pdf or other document programs, we cannot directly make transliteration process 
             happen. Firstly, we need to import the images, read the text from that image and pass the read data to the transliteration 
             process.
             Reading text from an image is called Optical Character Recognition (OCR) and comprises the main part. The output of this step is 
             in a string format.
             The output in a string format from the OCR tool is the proceed into the next part in which each character in Cyrillic format is 
             replaced with its Latin equivalent.
             """)

