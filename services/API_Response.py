from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv("my_api_key.env") # give this function call a string path to the location of api key
gemini_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_key)
def gemini_response(user_tasks, user_instructions):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Given the following tasks: {user_tasks}, use the following instructions. {user_instructions}",
    config=types.GenerateContentConfig(thinking_config=types.ThinkingConfig(thinking_budget=0))
    # Disabled thinking to keep costs low and also so i don't waste as many tokens
)
    return response
