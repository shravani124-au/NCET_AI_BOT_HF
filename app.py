import streamlit as st
from transformers import pipeline
@st.cache_resource
def load_summarize():
return pipeline("summerization",model="sshleifer/distilbart-cnn-12-6")
sumarize=load_sumarizer()
st.title("ai text summarizer")
st.write("enter a long text below,and get a concise sumary!")
max_length = st.slider("Max Summary Length", min_value=50, max_value=300, value=130)
min_length = st.slider("Min Summary Length", min_value=20, max_value=100, value=30)

if st.button("Summarize"):
    if long_text:
        summary = summarizer(long_text, max_length=max_length, min_length=min_length, do_sample=False)
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text!")





