#!/usr/bin/python3

"""This file defines the Amenity model
   It inherits from the BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity Model"""

    # Attributes
    name: str = ""
