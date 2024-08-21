# Importing the required packages
import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core import output_parsers
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Loading the environment variables from the .env file
load_dotenv()

# Assign the API key to the environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")

# Defining the Prompt templates
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an Intelligent System which can answer\
        any questions based on the LLM and AI and you are going to\
        answer all the question which are raised by the user about it.",
        ),
        ("user", "Question: {question}"),
    ]
)

# Streamlit app
st.title("LangChain's Chatbot")
input_text = st.text_input("Enter your question here:")

# Calling the OpenAI model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Setting the output_parsers
output_parsers = StrOutputParser()

# Creating the Chain of the Chatbot
chain = prompt | llm | output_parsers

# Getting the response from the Chatbot
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
