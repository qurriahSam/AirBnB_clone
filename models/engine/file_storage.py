#!/usr/bin/python3

import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns all objects stored """
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__
        self.__objects.update({f"{key}.{obj.id}": obj})

    def save(self):
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        try:
            with open(self.__file_path, mode="r") as f:
                jo = json.load(f)
                for k in jo:
                    self.__objects[k] = classes[jo[k]["__class__"]](**jo[k])
        except FileNotFoundError:
            return
