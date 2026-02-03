from sqlalchemy import (Column,String,Integer,Text,Enum,DateTime,JSON,Boolean,)
from sqlalchemy.sql import func
from app.models.base import Base
from app.models.dermatologist import DermatologistStatus


class DermatologistProfile(Base):
    
    __tablename__ = "dermatologist_profiles"
    
    user_id = Column(String, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    clinic_name = Column(String(255), nullable=True)
    bio = Column(Text, nullable=True)
    
    profile_image_url = Column(String, nullable=False)
    
    phone_number = Column(String(30), nullable=False)
    is_phone_verified = Column(Boolean, default=False)
    
    email = Column(String(255), nullable=False)
    is_email_verified = Column(Boolean, default=False)
    
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    address = Column(Text, nullable=True)
    specializations = Column(JSON, nullable=False)  # ["acne", "eczema"]
    years_of_experience = Column(Integer, nullable=True)
    license_number = Column(String(100), nullable=False)
    consultation_price = Column(Integer, nullable=True)
    offers_online_consultation = Column(Integer, default=0)
    social_links = Column(JSON, nullable=False)
    status = Column(
        Enum(DermatologistStatus),
        default=DermatologistStatus.pending,
        nullable=False,
    )
    rejection_reason = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    verified_at = Column(DateTime(timezone=True), nullable=True)