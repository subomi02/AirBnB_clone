#!/usr/bin/python3
'''File Storage file'''
import json
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage():
    '''FileStorage Class'''

    def __init__(self):
        '''__init__'''
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        '''return __objects'''
        return (self.__objects)

    def new(self, obj):
        '''new obj'''
        self.__objects[
            "{}.{}".format(obj.__class__.__name__, obj.id)
            ] = obj

    def save(self):
        '''save json'''
        dict_exp = {
                        obj: self.__objects[obj].to_dict()
                        for obj in self.__objects.keys()
        }
        json_exp = open(self.__file_path, "w")
        json_exp.write(json.dumps(dict_exp))
        json_exp.close()

    def reload(self):
        try:
            json_reload = open(self.__file_path, "r")
            json_old = json.loads(json_reload.read())
            json_reload.close()
            for key, value in json_old.items():
                value = eval(value["__class__"])(**value)
                self.__objects[key] = value
        except FileNotFoundError:
            pass
