from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.models.base import Base

class DermatologistDocument(Base):
    __tablename__ = "dermatologist_documents"
    
    id = Column(String, primary_key=True)
    dermatologist_id = Column(
        String,
        ForeignKey("dermatologist_profiles.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    
    document_type = Column(String(100), nullable=False)
    file_url = Column(String, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())