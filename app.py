### Simple Gen AI app using Langchain
import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "")
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework
st.title("Langchain with LLAMA Model")
input_text = st.text_input("What question is in your mind?")

## Ollama model (example: llama2 or gemma:2b)
llm = Ollama(model="llama2")  # or "llama2"

## Output parser
output_parser = StrOutputParser()

## Create chain
chain = prompt | llm | output_parser

## Handle user input
if input_text:
    st.write(chain.invoke({"question": input_text}))

