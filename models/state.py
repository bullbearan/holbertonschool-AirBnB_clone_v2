#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
import models
from models.city import City


class State(BaseModel):
    """This is a class"""
    name = ""
