import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class DetectionLog(Base):
    __tablename__ = "detection_logs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_size = Column(Integer)
    media_type = Column(String)
    result = Column(String)
    confidence_score = Column(Float)
    processing_time = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)