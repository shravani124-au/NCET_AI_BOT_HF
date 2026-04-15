import streamlit as st
from transformers import pipeline
@st.cache_resource
def load_summarize():
return pipeline("summerization",model="sshleifer/distilbart-cnn-12-6")
