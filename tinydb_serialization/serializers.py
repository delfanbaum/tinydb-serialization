from datetime import datetime
from pathlib import Path

from tinydb_serialization import Serializer


class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime  # The class this serializer handles

    def encode(self, obj):
        return obj.isoformat()

    def decode(self, s):
        return datetime.fromisoformat(s)


class PathSerializer(Serializer):
    """ relative to working directory """
    OBJ_CLASS = Path

    def encode(self, obj):
        return str(obj)

    def decode(self, s):
        return Path(s)
