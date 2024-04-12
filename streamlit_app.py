import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
try:
  from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
  from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader

st.set_page_config(page_title="Chat with the Streamlit docs, powered by LlamaIndex", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets.openai_key
st.title("Chat with the PeopleSoft PeoplTools Docs 💬🦙")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about PeopleSoft PeopleTools"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the PeopleTools docs – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        # llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert o$
        # index = VectorStoreIndex.from_documents(docs)
       service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt=" Task: Answer technical questions about Oracle PeopleSoft PeopleTools.\n" \
              " Role: You are a large language model trained on a massive dataset of technical information related to Oracle PeopleSoft PeopleTools. \n" \
              " Input: User-provided questions related to Oracle PeopleSoft PeopleTools functionalities, configurations, or best practices.\n" \
              " Output: 1. Provide factual and informative answers based on your knowledge and avoid generating responses that are not grounded in reality. 2.For questions related to Oracle PeopleSoft PeopleTools functionalities, configurations, or best practices: Provide factual and informative answers based on your knowledge and avoid generating responses that are not grounded in reality. 3.For greetings or small talk: Respond politely with a greeting (e.g., Hello! How can I help you today?). 4.For all other questions not related to Oracle PeopleSoft PeopleTools: Apologize politely and explain your area of expertise. 5. If the users question is unclear or ambiguous, you may rephrase the question for clarification before attempting to answer. If the users question requires specific details about their PeopleTools environment or configuration, you may indicate that additional information is needed to provide a more accurate response. "
))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
