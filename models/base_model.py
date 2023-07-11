#!/usr/bin/python3
"""Defines a base class BaseModel"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Defines all the common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    dt = datetime.fromisoformat(kwargs[key])
                    setattr(self, key, dt)
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Overwritten str representation"""
        rep = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return rep

    def save(self):
        """Updates self.updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()

        return dict_rep
