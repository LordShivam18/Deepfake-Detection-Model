from sqlalchemy.orm import Session
from . import models, schemas

def create_detection_log(db: Session, log: schemas.DetectionLogCreate):
    db_log = models.DetectionLog(**log.model_dump())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log