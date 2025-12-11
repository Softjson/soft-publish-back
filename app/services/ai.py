from google import genai 
from app.core.config import settings

client = genai.Client(api_key=settings.gemini_api_key)

def generate_post(topic: str, style: str):
    prompt = f"""
    Genera una publicación corta para Instagram sobre el tema '{topic}'.
    Estilo: {style}.
    Mantén un tono profesional, creativo, claro y atractivo.
    """

    response = client.models.generate_content( 
        model="gemini-2.5-flash", contents=prompt
        )

    return response.text
