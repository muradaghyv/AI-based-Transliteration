import streamlit as st
from email.message import EmailMessage
import ssl
import smtplib

st.title("Sending Transliteration via Gmail!")

if "latin_cyril" in st.session_state:
    email_sender = "agayev.m2002@gmail.com"
    email_password = "aaku gufo lswj ekqx"
    receiver = st.text_input("Please input your email address:")
    if "receiver":
        subject = "Transliterated text"
        body = st.session_state["latin_cyril"]
        
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = receiver
        em["Subject"] = subject
        em.set_content(body)
        
        context = ssl.create_default_context()
        
        if st.button("Send email!"):
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, receiver, em.as_string())
            st.success("Email sent successfully!")
    else:
        st.error("Please enter the valid email address!")
else:
    st.error("Make the process before sending it!")