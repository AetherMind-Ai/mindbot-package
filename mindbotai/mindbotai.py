import google.generativeai as mindai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MIND_API_KEY")
if not api_key:
    raise ValueError("MIND_API_KEY environment variable not set")

mindai.configure(api_key=api_key)
mindbot1_3= "gemini-1.5-flash"

def generate_content(prompt):
    model = mindai.GenerativeModel(mindbot1_3)
    response = model.generate_content(prompt)
    return response.text
