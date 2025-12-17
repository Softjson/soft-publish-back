from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class PostTemplate(Base):
    __tablename__ = "post_templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    prompt_template = Column(Text, nullable=False)
