from pydantic import BaseModel

class TemplateCreate(BaseModel):
    name: str
    description: str
    prompt_template: str
