#!/usr/bin/python3
"""State module
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """State Object Mapped to states table
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
        )

    name = Column(String(128), nullable=False)
