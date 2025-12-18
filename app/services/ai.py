from google import genai 
from app.core.config import settings
from google.genai.errors import ServerError

client = genai.Client(api_key=settings.gemini_api_key)

def generate_post(prompt: str) -> str:
    try:
        for model in client.models.list():
            print(f"Modelo disponible: {model.name}")
        response = client.models.generate_content( 
            model="gemini-2.0-flash-lite", contents=prompt)
        return response.text
    except ServerError:
        return "El modelo de IA está temporalmente ocupado. Intenta nuevamente."