import base64
import io
from PIL import Image
import pdf2image

# Function to process uploaded PDF file
def process_uploaded_pdf(uploaded_file):
    if uploaded_file is not None:

        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]


        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() # encode to base64
            }
        ]
        return pdf_parts
    return None 