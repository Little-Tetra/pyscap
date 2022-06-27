from enum import Enum


class CVEStatus(str, Enum):
    candidate = "CANDIDATE"
    entry = "ENTRY"
    deprecated = "DEPRECATED"
