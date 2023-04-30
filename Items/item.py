from enum import Enum
from stat_class import Stat    
            
class Item:
    def __init__(self, item_name: str,
                 item_modifiers: dict = {Stat.NONE: 0},
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
        
    def Item_Examination(self):
        print(f"{self.name}: {self.description}")