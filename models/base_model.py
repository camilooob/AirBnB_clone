# /usr/bin/python3
""" Modules for Class """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ Class BaseModel """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """ Building Class """
        if (len(kwargs) is not 0):
            for key, value in kwargs.items():
                if (key == 'id'):
                    self.id = kwargs.get(key)
                if (key == 'created_at'):
                    self.created_at = datetime.strptime(
                        kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
                if (key == 'updated_at'):
                    self.updated_at = datetime.strptime(
                        kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String Method """
        return ("[{self.__class__.__name__}] ({}) {}"
                .format(self.id, self.__dict__, self=self))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a Dictionary """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return(new_dict)
