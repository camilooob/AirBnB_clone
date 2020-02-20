#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ Class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return Objects """
        return (FileStorage.__objects)

    def new(self, obj):
        """ Create New Object """
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Save File Json """
        with open(FileStorage.__file_path, 'w') as file_json:
            res = {}
            for key, value in FileStorage.__objects.items():
                res[key] = value.to_dict()
            file_json.write(json.dumps(res))

    def reload(self):
        """ Reload File Json """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file_json:
                from models.base_model import BaseModel
                from models.user import User
                json_des = json.load(file_json)
            for key in json_des.keys():
                # search "__class__": "BaseModel"
                inst_dict = json_des[key]
                inst_class = inst_dict['__class__']
                self.__objects[key] = BaseModel(json_des[key])
