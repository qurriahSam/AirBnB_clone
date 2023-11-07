from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
        Defines all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        print(f"[{self.__class__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__.copy()

        dict['__class__'] = self.__class__
        return dict
