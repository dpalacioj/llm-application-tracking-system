import google.generativeai as genai

class GeminiModel:
    def __init__(self, api_key, model_name='gemini-1.5-flash-001'):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.config = genai.GenerationConfig(
        temperature= 0.2,
        max_output_tokens=500,
        top_p=0.9,
        top_k = 40
        )

    def get_response(self, input_text, pdf_content, prompt):
        response = self.model.generate_content(
            [input_text, pdf_content[0], prompt],
            generation_config=self.config
        )
        return response.text