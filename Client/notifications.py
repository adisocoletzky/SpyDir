from enum import Enum


class Notification(Enum):
    ZIP_INIT = 0
    FILE_CREATED = 1
    DIR_CREATED = 2
    FILE_DELETED = 3
    DIR_DELETED = 4
    FILE_MODIFIED = 5
    DIR_MODIFIED = 6
