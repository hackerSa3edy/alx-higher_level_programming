#!/usr/bin/python3
"""City Module
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City Object Mapped to cities table
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
        )

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
