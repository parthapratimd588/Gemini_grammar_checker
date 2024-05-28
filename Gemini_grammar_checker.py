import google.generativeai as genai
import streamlit as st
from redlines import Redlines
from IPython.display import display, Markdown

def geminiFunction(system_prompt, user_prompt):
  gemini_api_key = str("AIzaSyCLzRcf5YrMmul3VDgaqoWX285t__q3A8w")
  genai.configure(api_key = gemini_api_key)
  model = genai.GenerativeModel("gemini-pro")
  chat_complition = model.generate_content([system_prompt, user_prompt])
  response = chat_complition.text
  return response
system_prompt = "Your task is to generate multiple proofread and correct of the given query."
#query = st.text_input("Input here", placeholder = "Ask me!")
user_prompt = st.text_input("Enter your querry here.")

if user_prompt:
    response = geminiFunction(system_prompt, user_prompt)
  
    diff = Redlines(user_prompt, response)
    

    st.markdown(":blue[Query:]")
    st.markdown(user_prompt)
    st.markdown(":green[Response: ]")
    st.markdown(diff.output_markdown, unsafe_allow_html = True)