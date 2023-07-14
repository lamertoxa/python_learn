from os import path
import json
import pickle
from enum import Enum
class FileType(Enum):
    JSON = "1"
    BYTE = "2"
class SerializeManager():
    def __init__(self, filename, fileType):
        self.filename = filename
        self.fileType = fileType
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    def serialize(self, object):
        if self.fileType.value == "1":
            with open(self.filename, "w") as f:
                json.dump(object, f)
        if self.fileType.value == "2":
            with open(self.filename, "wb") as f:
                pickle.dump(object, f)


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)