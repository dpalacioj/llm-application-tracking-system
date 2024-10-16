# Import required libraries
from dotenv import load_dotenv
import streamlit as st
import base64
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


# Function to get response from Gemini model
def get_geimini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-001')
    config = genai.GenerationConfig(
        temperature= 0.2,
        max_output_tokens=500,
        top_p=0.9,
        top_k = 40
    )
    response = model.generate_content(
        [input_text, pdf_content[0], prompt], generation_config=config
    )
    return response.text

# Function to process uploaded PDF file
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        # Prepare PDF content for Gemini model
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

# Streamlit App Configuration

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# User Inputs
input_text=st.text_area("Job Description:", key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Action Buttons
submit1= st.button("Tell me about the resume")
submit2 = st.button("Percentage match")

# Prompts for different analyses
input_prompt1 = """
    You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
    Please share your professional evaluation on whether the candidate's profile aligns with the role. 
    Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
    The roles will be associated with tecnologies fiels, focusing on data science and machine learning.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

# Handle button actions
if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_geimini_response(input_prompt1, pdf_content,input_text)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_geimini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload the resume")