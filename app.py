
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"),credentials=)
model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content('Teach me about how an LLM works')
# print(response.text)

def get_model_response(prompt):
    my_id = "my-tuned-model-id"
    operation = genai.create_tuned_model(
    id = my_id,
    source_model= 'models/gemini-1.5-flash',
    training_data=[('hi', 'Atharva')]
    )
    tuned_model=operation.result()      # Wait for tuning to finish

    response = genai.generate_text(f"tunedModels/{my_id}", prompt="")
    return response



user_input = input()

print(get_model_response(user_input))

# def get_gemini_response(input,prompt): #input tell what should model do, image is the image we are passing, propmt the answe we want 

#     response = model.generate_content([input,prompt]) 
#     return response.text

# input_prompt ="""

# You are an expert in answering customer queries. You can't do oth
# """

# print(get_gemini_response(input_prompt,input())c)