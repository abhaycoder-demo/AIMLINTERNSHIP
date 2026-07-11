from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_KEY")

client = genai.Client(api_key=API_KEY)
result = client.models.generate_content(model='gemini-3.5-flash', contents='Write a short poem about the beauty of nature.')
print (result.text)