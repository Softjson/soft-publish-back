from sqlalchemy import Column, Integer, String, Text, DateTime, func 
from app.db.base import Base

class GeneratedPost(Base):
    __tablename__ = "generated_posts"
    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String(255), nullable=False)
    style = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    template_key = Column(String, nullable=False)
