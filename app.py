import streamlit as st
from chatbot import handle_query

def run_chatbot():
    st.title("Multilingual Chatbot")
    st.write("I can respond in English, Spanish, French, and Hindi!")

    user_query = st.text_input("Your question:")
    if user_query:
        response = handle_query(user_query)
        st.write("Chatbot Response:")
        st.write(response)

if __name__ == "__main__":
    run_chatbot()
