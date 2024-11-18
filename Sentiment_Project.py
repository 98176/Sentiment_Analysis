import streamlit as st
st.sidebar.title("About Us")
st.sidebar.text("""We are students at ducat &
learning machine learning.
""")

st.sidebar.title("contact us")
st.sidebar.text("""Sonu @ 1111
Monu @ 22222
Chintu @ 3333
""")



st.title("Sentiment Analysis")
text=st.text_input("**Enter text**")
btn=st.button("Predict")

from textblob import TextBlob

if btn:
    blob=TextBlob(text)
    sent=blob.sentiment[0]
    if sent<0:
        st.error("Negative Sentiment")
        st.image("E:/Machine_Learning_by_Aditya_Sir/Streamlit-programming/negative.png")
    elif sent>0:
        st.success("Positive Sentiment")
        st.image("E:/Machine_Learning_by_Aditya_Sir/Streamlit-programming/positive.png")
    else:
        st.warning("Neutral Sentiment")
        st.image("E:/Machine_Learning_by_Aditya_Sir/Streamlit-programming/neutral.png")
        
        
