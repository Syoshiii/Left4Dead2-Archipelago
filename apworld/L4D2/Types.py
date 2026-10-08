from typing import NamedTuple, Optional
from BaseClasses import Location, Item, ItemClassification

class L4D2Location(Location):
    game = "Left 4 Dead 2"

class APSkeletonItem(Item):
    game = "Left 4 Dead 2"

class ItemData(NamedTuple):
    ap_code: Optional[int]
    classification: ItemClassification
    count: Optional[int] = 63

class LocData(NamedTuple):
    code: int
    name: str
    type: str
