import pytesseract
import streamlit as st
import time 

st.title("OCR & Transliteration Process!")

custom_config = r"--oem 3 --psm 6 -l aze_cyrl"

def ocr_translit(image, language_based="aze_cyrl", config = custom_config):
    
    cyrillic_text = pytesseract.image_to_string(image, lang=language_based)
    
    custom_mapping = {
    "Ј":"Y", "Ү":"Ü", "У":"U", "К":"K", "Е":"E", "Н":"N", "Г":"Q", "Ш":"Ş", "Һ":"H", "З":"Z", "Х":"X", "Ҹ":"С",   
    "Ф":"F", "Ы":"I", "В":"V", "А":"A", "П":"P", "Р":"R", "О":"O", "Л":"L", "Д":"D", "Ж":"J", "Ҝ":"G", "Ә":"Ə",
    "Ч":"Ç", "С":"S", "М":"M", "И":"İ", "Т":"T", "Ғ":"Ğ", "Б":"B", "Ө":"Ö",
    "ј":"y", "ү":"ü", "у":"u", "к":"k", "е":"e", "н":"n", "г":"q", "ш":"ş", "һ":"h", "з":"z", "х":"x", "ҹ":"c",   
    "ф":"f", "ы":"ı", "в":"v", "а":"a", "п":"p", "р":"r", "о":"o", "л":"l", "д":"d", "ж":"j", "ҝ":"g", "ә":"ə",
    "ч":"ç", "с":"s", "м":"m", "и":"i", "т":"t", "ғ":"ğ", "б":"b", "ө":"ö",
  
    "я":"ə", "ц":"ü", "й":"y", "ь":"ğ", "э": "ə", "Э": "Ə", "Ъ":"h", "]": "y", "/":"y", "{":"y", "\\":"y", "|":"y", 
    "(":"y", ")":"y", "}":"y"
    }
    
    latin_text = ''.join(custom_mapping.get(char, char) for char in cyrillic_text) 
    latin_text = latin_text.replace("tp", "ş") 
    latin_text = latin_text.replace("oe", "ə")
    
    return cyrillic_text, latin_text

if "img_modif" or "img" in st.session_state:
    image = st.session_state["final"]
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    if st.button("Begin the process!"):
        progress_text = "Model in process . . ."
        bar = st.sidebar.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            bar.progress(percent_complete+1, text=progress_text)
        bar.empty()
        
        cyrillic_text, latin_text_cyril = ocr_translit(image)
        
        russian_text, latin_text = ocr_translit(image, language_based="rus")
        
        st.session_state["cyrillic"] = cyrillic_text
        st.session_state["latin"] = latin_text
        st.session_state["latin_cyril"] = latin_text_cyril
    
    option = st.selectbox("Choose text format:",
                          ("-", "Cyrillic text", "Latin text", "Latin text - Cyril"))
    
    if option == "Cyrillic text":
        if "cyrillic" in st.session_state:
            st.code(st.session_state["cyrillic"], language="text")
        else:
            st.error("OCR process has not done properly!")
            
    elif option == "Latin text":
        if "latin" in st.session_state:
            st.code(st.session_state["latin"], language="text")
        else:
            st.error("OCR process has not done properly!")
        
    elif option == "Latin text - Cyril":
        if "latin_cyril" in st.session_state:
            st.code(st.session_state['latin_cyril'], language="text")
        else:
            st.error("OCR process has not done properly!")

    