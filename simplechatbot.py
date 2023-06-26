import streamlit as st
from llama_index import StorageContext, load_index_from_storage
import openai
from dotenv import load_dotenv
import os
from streamlit_chat import message
import streamlit.components.v1 as components

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get the chatbot response
def get_chatbot_response(question):
    try:
        # Rebuild the storage context
        persist_dir = "E:\ThanhTam_DA\Project\chatbot"  # Specify the directory path where you saved the index files
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)

        # Load the index from the index_store.json file
        index = load_index_from_storage(storage_context, file_name="index_store.json")

        # Query the index for the given question
        query_engine = index.as_query_engine()
        response = query_engine.query(question)

        return response.response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit app
def main():
    st.title("데이터사이언스 챗봇")

    # Input text box for user input
    user_input = st.text_input("당신")

    # Button to submit user input and get response
    if st.button("전송"):
        if user_input:
            bot_response = get_chatbot_response(user_input)
            if bot_response:
                st.session_state.past.append(user_input)
                st.session_state.generated.append(bot_response)
            else:
                st.warning("No response found.")
        else:
            st.warning("Please enter a question.")

    for i in range(len(st.session_state['past'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        if len(st.session_state['generated']) > i:
            message(st.session_state['generated'][i], key=str(i) + '_bot')

# Initialize chat history in Streamlit session state
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

# Run the Streamlit app
if __name__ == "__main__":
    main()
