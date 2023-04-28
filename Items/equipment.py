from Items.item import *

class Equipment_Slot(Enum):
    HEAD = 1
    SHOULDERS = 2
    CHEST = 3
    HANDS = 4
    WEAPON = 5
    SHIELD = 6
    LEGS = 7
    FEET = 8
    NONE = 9

class Equipment(Item):
    def __init__(
        self,
        name: str,
        equipment_slot: Equipment_Slot,
        modifier: dict,
        description: str = "Some old equipment, I guess...",
        value: int = 1):
        
        super().__init__( name, modifier, description, value )
        
        self.equipment_slot = equipment_slot
        