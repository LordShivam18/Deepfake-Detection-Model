import datetime
from pydantic import BaseModel

class DetectionLogBase(BaseModel):
    filename: str
    file_size: int
    media_type: str
    result: str
    confidence_score: float
    processing_time: float

class DetectionLogCreate(DetectionLogBase):
    pass

class DetectionLog(DetectionLogBase):
    id: int
    timestamp: datetime.datetime

    class Config:
        from_attributes = True