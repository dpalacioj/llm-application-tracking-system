# Import required libraries
from dotenv import load_dotenv
import streamlit as st
import os

# Personalized Modules
from models.gemini_model import GeminiModel
from utils.pdf_processor import process_uploaded_pdf
from utils.prompt_templates import evaluation_prompt, percentage_prompt


# Load environment variables
load_dotenv()

# Configure Google API
api_key = os.getenv("GOOGLE_API_KEY")


# Choose a model
def get_model(model_name):
    if model_name == 'gemini':
        return GeminiModel(api_key=api_key)
    elif model_name == 'mistral':
        return MistralModel(api_key=mistral_api_key)
    ## Add models as you need it
    else:
        raise ValueError(f"Model not supported: {model_name}")


# Streamlit App Configuration
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# Select the model since the web interface
model_options = ['gemini', 'mistral'] # add as many you need
selected_model_name = st.sidebar.selectbox("Choose one model", model_options)

# Set up the model
model = get_model(selected_model_name)

# User Inputs
input_text=st.text_area("Job Description:", key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Action Buttons
submit1= st.button("Tell me about the resume")
submit2 = st.button("Percentage match")

# Handle button actions
if submit1:
    if uploaded_file is not None:
        resume_content = process_uploaded_pdf(uploaded_file)
        response = model.generate_response(input_text, resume_content, evaluation_prompt)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        resume_content = process_uploaded_pdf(uploaded_file)
        response = model.generate_response(input_text, resume_content, percentage_prompt)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload the resume")