#!/usr/bin/python3

import json


class FileStorage:
    __file_path = ""
    __objects = {}

    def all(self):
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
                for obj in jo.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return






