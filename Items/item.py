from enum import Enum
    
class Item_Stat_Modifier(Enum):
    LEVEL = 1
    EXPERIENCE = 2
    HEALTH_MAX = 3
    HEALTH_CUR = 4
    ATTACK_POWER = 5
    ATTACK_SPEED = 6
            
class Item:
    def __init__(self, item_name: str,
                 item_modifiers: dict,
                 item_description: str = "Item lacks description",
                 value: int = 1):
        if not isinstance(item_name, str):
            raise TypeError("Item Name must be a string")
        if not isinstance(item_modifiers, dict):
            raise TypeError("Item Modifiers must be stored in a dictionary")
        self.name = item_name
        self.modifiers = item_modifiers
        self.description = item_description
        self.value = value
        