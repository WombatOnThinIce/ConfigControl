import datetime

from constants import *


def create_log_entry(notes: str) -> dict[str, str]:
    return {"date": datetime.datetime.now(tz=datetime.UTC).isoformat(), "note": notes}

class Version:
    def __init__(self, serial: int, notes: str) -> None:
        self.created = datetime.datetime.now(tz=datetime.UTC).isoformat()
        self.status_last_changed = None
        self.status = STATUSES[1]
        self.version = serial
        self.log = [create_log_entry(f"VERSION_CREATED V{self.version}>> " + notes)]

    def change_status(self, new_status: str, notes: str) -> None:
        if new_status not in STATUSES:
            raise ValueError('Status type must be allowed')
        else:
            self.log.append(create_log_entry(f"STATUS_CHANGE - from {self.status} to {new_status}>> " + notes))
            self.status = new_status
            self.status_last_changed = datetime.datetime.now(tz=datetime.UTC).isoformat()

class ConfigItem:
    def __init__(self, type: str, serial: int, name: str, ci_id: str, creation_notes: str) -> None:
        if type not in CI_TYPES:
            raise ValueError('CI type must be allowed')
        else:
            self.created = datetime.datetime.now(tz=datetime.UTC).isoformat()
            self.version_last_added = None
            self.creation_notes = creation_notes
            self.name = name
            self.serial = serial
            self.ci_id = ci_id
            self.type = type
            self.log = [create_log_entry(f"CI_CREATED - type {self.type}>> " + creation_notes)]
            self.versions = [Version(1, f"CI_CREATED - type {self.type}>> " + creation_notes)]

    def add_new_version(self, notes: str) -> Version:
        new_serial = len(self.versions) + 1
        new_version = Version(new_serial, notes)
        self.versions.append(new_version)
        self.log.append(create_log_entry(f"VERSION_CREATED V{new_version}>> " + notes))
        self.version_last_added = datetime.datetime.now(tz=datetime.UTC).isoformat()
        return new_version

class Project:
    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number
        self.proj_id = f"P{self.number}"
        self.created = datetime.datetime.now(tz=datetime.UTC).isoformat()
        self.ci_last_added = None
        self.log = [create_log_entry(f"PROJECT_CREATED - {self.number} - {self.name}>> ")]
        self.cis = []

    def generate_ci_id(self, serial) -> str:
        return f"{self.proj_id}-C{serial}"

    def add_new_ci(self, type: str, name: str, notes: str) -> ConfigItem:
        new_serial = len(self.cis) + 1
        new_ci_id = self.generate_ci_id(new_serial)
        new_ci = ConfigItem(type, new_serial, name, new_ci_id, notes)
        self.cis.append(new_ci)
        self.log.append(create_log_entry(f"CI_CREATED CI-{new_serial}>> " + notes))
        self.ci_last_added = datetime.datetime.now(tz=datetime.UTC).isoformat()
        return new_ci
