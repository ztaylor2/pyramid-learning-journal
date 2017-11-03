from sqlalchemy import (
    Column,
    Date,
    Float,
    Integer,
    Unicode,
)


# from datetime import datetime
from .meta import Base


class Entry(Base):
    """Entry model class."""
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(Date)


# Index('my_index', MyModel.name, unique=True, mysql_length=255)