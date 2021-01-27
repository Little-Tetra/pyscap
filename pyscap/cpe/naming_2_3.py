from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Cpe22Type:
    """Define the format for acceptable CPE Names.

    A URN format is used with the id starting with the word cpe followed
    by :/ and then some number of individual components separated by
    colons.
    """

    class Meta:
        name = "cpe22Type"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}",
        }
    )


@dataclass
class Cpe23Type:
    """Define the format for acceptable CPE Names.

    A string format is used with
    the id starting with the word cpe:2.3 followed by : and then some number of individual components
    separated by colons.
    """

    class Meta:
        name = "cpe23Type"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": "cpe:2\\.3:[aho\\*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#$$%&'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|}~]))+(\\?*|\\*?))|[\\*\\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[\\*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#$$%&'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|}~]))+(\\?*|\\*?))|[\\*\\-])){4}",
        }
    )
