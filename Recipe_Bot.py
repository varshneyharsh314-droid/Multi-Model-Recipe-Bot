from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import PromptTemplate
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
import streamlit as st
import time
from dotenv import load_dotenv

load_dotenv()

st.header('Multi model Recipe Bot')
st.markdown("")

user_input = st.text_input('Enter your prompt')

model_input = st.selectbox("Select model Name", ["Google Gemini", "Groq"])

col1, col2 = st.columns([1, 0.40])

with col1:
    submit_btn = st.button("Submit")

with col2:
    compare_button = st.button("Compare Gemini vs Groq")
    

model1 = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

model2 = ChatGroq(
    model="llama-3.1-8b-instant"
)

prompt1 = PromptTemplate(
    template='Give me the {topic}',
    input_variables=['topic']
)

class Review(BaseModel):

    recipe_name: str = Field(description="Write down the name of the recipe")
    ingredients: list[str] = Field(description="Write down all the ingredients used in the recipe")
    steps: list[str] = Field(description="write down all the steps used in the recipe")
    cooking_time: str = Field(description="Write down the time required to prepare the recipe")
    difficulty_level: str = Field(description="Write down the difficulty level of the recipe")
    nutrition_facts: dict[str,str] = Field(description="Write down the nutrition  facts in the recipe in  the dictionary format")
    
structured_model1 = model1.with_structured_output(Review)
structured_model2 = model2.with_structured_output(Review)

if submit_btn:
    messages = [
        SystemMessage(content="You are a helpful AI Chef that only responds in valid JSON matching the Review schema."),
        HumanMessage(content=user_input)
    ]
    if(model_input=="Google Gemini"):
        result=structured_model1.invoke(messages)
        
    if(model_input=="Groq"):
        result=structured_model2.invoke(messages)
    
    st.subheader("Generated Recipe:")
    st.json(result)

if compare_button and user_input:
    messages = [
        SystemMessage(content="You are a professional chef who outputs recipe details in structured JSON."),
        HumanMessage(content=user_input)
    ]
    
    start_gemini = time.time()
    result_gemini = structured_model1.invoke(messages)
    end_gemini = time.time()
    time_gemini = end_gemini - start_gemini

    start_groq = time.time()
    result_groq = structured_model2.invoke(messages)
    end_groq = time.time()
    time_groq = end_groq - start_groq

    st.subheader(" Gemini Output")
    st.json(result_gemini)
    st.write(f"Time: {time_gemini:.2f} sec ")

    st.subheader(" Groq Output")
    st.json(result_groq)
    st.write(f"Time: {time_groq:.2f} sec")