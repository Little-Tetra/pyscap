import re
from typing import List

from pydantic import BaseModel, validator

from .enums import CVEStatus


class CVE(BaseModel):
    id: str
    status: CVEStatus = None
    description: str = None
    references: List[str] = []

    @validator('id')
    def check_cve_id_format(cls, v):
        if re.fullmatch(r"CVE-([1,2])\d{3}-\d{4,7}", v) is None:
            raise ValueError("Incorrect CVE id format")
        return v
