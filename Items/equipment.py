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
        
    def Equipment_Slot_To_String(slot: Equipment_Slot):
        if slot == Equipment_Slot.HEAD:
            return "head"
        if slot == Equipment_Slot.SHOULDERS:
            return "shoulders"
        if slot == Equipment_Slot.CHEST:
            return "chest"
        if slot == Equipment_Slot.HANDS:
            return "hands"
        if slot == Equipment_Slot.WEAPON:
            return "weapon"
        if slot == Equipment_Slot.SHIELD:
            return "shield"
        if slot == Equipment_Slot.LEGS:
            return "legs"
        if slot == Equipment_Slot.FEET:
            return "feet"
        if slot == Equipment_Slot.NONE:
            return "none"
        