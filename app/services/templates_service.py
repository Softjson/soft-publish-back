POST_TEMPLATE_INSTAGRAM = """
Genera una publicación corta para Instagram sobre el tema "{topic}".
Estilo: {style}.
Mantén un tono profesional, creativo, claro y atractivo.
"""

def build_prompt(template: str, topic: str, style: str) -> str:
    return template.format(topic=topic, style=style)