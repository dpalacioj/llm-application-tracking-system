# LLM Application Tracking System

This application is an AI-powered ATS (Application Tracking System) that uses Google's Gemini model to analyze resumes against job descriptions, providing detailed evaluations and match percentages.

## Features

- **Resume Analysis**: Upload PDF resumes and get AI-powered evaluation
- **Dual Analysis Modes**:
  - **Professional Evaluation**: Detailed assessment of candidate's strengths and weaknesses
  - **Percentage Match**: Numerical score with missing keywords and recommendations
- **User-friendly Interface**: Simple Streamlit web app for easy interaction
- **PDF Processing**: Automatic extraction and conversion of resume content

## Prerequisites

- Python 3.x
- Google Gemini API key
- Poppler-utils (required by pdf2image)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/llm-application-tracking-system.git
   cd llm-application-tracking-system

2. Install required Python packages:

   `pip install -r requirements.txt`

3. Install poppler-utils (for PDF processing):

* Ubuntu/Debian: `sudo apt-get install poppler-utils`
* Fedora: `sudo dnf install poppler-utils`
* macOS: `brew install poppler`

## Configuration

1. Rename `env-sample.txt` to `.env`:

`cp env-sample.txt .env`

2. Edit `.env` file and add your Google Gemini API key:

`GOOGLE_API_KEY=your_api_key_here`

## Usage

1. Start the application:

`streamlit run app.py`

## Project Structure
```bash
llm-application-tracking-system/
├── [app.py](http://_vscodecontentref_/0)                 # Main Streamlit application
├── models/
│   └── ai_model.py        # Google Gemini model integration
├── utils/
│   ├── pdf_processor.py   # PDF processing functions
│   └── prompt_templates.py # AI prompts for different analyses
├── [requirements.txt](http://_vscodecontentref_/1)       # Python dependencies
├── .env                   # Environment variables (not tracked by git)
└── [env-sample.txt](http://_vscodecontentref_/2)         # Sample environment variables