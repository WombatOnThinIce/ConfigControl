import datetime
from constants import *

class Version():
    def __init__(self, serial: int, creation_notes: str) -> None:
        self.timestamp = datetime.datetime.now(tz=datetime.UTC).isoformat()
        self.creation_notes = creation_notes
        self.status = STATUSES[1]
        self.version = serial

        if self.status not in STATUSES:
            raise ValueError('Status type must be allowed')

class ConfigItem():
    def __init__(self, type: str, serial: int, name: int, creation_notes: str) -> None:
        self.timestamp = datetime.datetime.now(tz=datetime.UTC).isoformat()
        self.creation_notes = creation_notes
        self.name = name
        self.type = type


class Project():
    def __init__(self, name: str) -> None:
        self.name = name
        self.number = issue_project_number()
