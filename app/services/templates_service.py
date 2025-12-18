TEMPLATES = {
    "instagram_post": """
    Genera una publicación para Instagram sobre '{topic}'.
    Estilo: {style}.
    Usa emojis moderadamente.
    Incluye hashtags relevantes al final.
    Tono claro, profesional y atractivo.
    """,

    "instagram_carrusel": """
    Genera un carrusel para Instagram sobre '{topic}'.
    Divide el contenido en 5 slides.
    Cada slide debe tener un título corto y texto claro.
    Estilo: {style}.
    """,

    "linkedin_post": """
    Genera un post para LinkedIn sobre '{topic}'.
    Estilo: {style}.
    Tono profesional, orientado a negocio y tecnología.
    Incluye un CTA suave al final.
    """,

    "instagram": """
    Genera una publicación para Instagram sobre "{topic}".
    Estilo: {style}.
    Usa emojis moderados.
    Incluye un llamado a la acción.
    No excedas 150 palabras.
    """,

    "linkedin": """
    Redacta una publicación profesional para LinkedIn sobre "{topic}".
    Estilo: {style}.
    Tono experto, claro y estratégico.
    Incluye reflexión final.
    """,

    "marketing": """
    Crea un copy de marketing persuasivo sobre "{topic}".
    Estilo: {style}.
    Enfocado en beneficios y conversión.
    """
}

def build_prompt(template_key: str, topic: str, style: str) -> str:
    template = TEMPLATES.get(template_key)
    if not template:
        raise ValueError("Template no encontrado")
    return template.format(topic=topic, style=style)