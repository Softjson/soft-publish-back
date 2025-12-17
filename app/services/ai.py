from google import genai 
from app.core.config import settings

client = genai.Client(api_key=settings.gemini_api_key)

def generate_post(prompt: str) -> str:
    response = client.models.generate_content( 
        model="gemini-2.5-flash", contents=prompt
        )

    return response.text
