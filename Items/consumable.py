from Items.item import *

class Consumbable(Item):
    def __init__(self, 
                 name: str,
                 modifiers: dict,
                 description: str = "Generic consumable",
                 value: int = 3):
        super().__init__(name, modifiers, description, value)