from sqlalchemy import (
    Column,
    Date,
    Integer,
    Unicode,
)

from .meta import Base


class Entry(Base):
    """Entry model class."""
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(Date)
