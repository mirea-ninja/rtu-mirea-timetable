import sqlalchemy as db
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class LessonCall(Base):
    __tablename__ = "schedule_lesson_call"

    id = db.Column(db.BigInteger, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    time_start = db.Column(db.Time, nullable=False)
    time_end = db.Column(db.Time, nullable=False)
    lesson = relationship(
        "Lesson",
        cascade="delete",
        back_populates="calls",
    )