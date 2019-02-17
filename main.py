from typing import List
from enum import Enum, auto
from lib230 import record, Factory


@record
class Cattle(Enum):
    """Represents the type of cattle

    """
    Matriarch = auto()
    Cow = auto()
    Bull = auto()
    calf = auto()


@record
class Herd:
    """Represents a herd of cattle

    """
    owner: str
    number_cattle: int
    matriarch: Matriarch
    field_time: int #hours in field
    stable_time: int #hours in stable
    herding_out: #time
    herding_in: #time


@record
class Tether:
    location: #(x,y)


@record
class Matriarch:
    """Represents the components of a Matriarch

    """
    current_position: #(x,y)
    max_dist_Tether: int


@record
class Cow:
    """Represents the components of a Cow

    """
    current_position: #(x,y)
    max_dist_MA: int
    response_to_breach: #shock,buzz,sound


@record
class Bull:
    """Represents the components of a Bull

    """
    current_position:  # (x,y)
    max_dist_MA: int
    response_to_breach:  # shock,buzz,sound


@record
class Calf:
    """Represents the components of a calf

    """
    current_position:  # (x,y)
    max_dist_MA: int
    response_to_breach:  # shock,buzz,sound

