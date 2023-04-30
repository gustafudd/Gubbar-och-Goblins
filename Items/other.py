from Items.item import *
from stat_class import Stat_To_String

class Interaction_Action(Enum):
    USE = 1
    BURY = 2
    NONE = 3
    
class Interaction_Result(Enum):
    NOTHING = 1
    DESTROY = 2
    MULTIPLY = 3
    
class Other(Item):
    def __init__(self, 
                 name: str,
                 interaction_action: Interaction_Action = Interaction_Action.NONE,
                 interaction_result: Interaction_Result = Interaction_Result.DESTROY,
                 modifiers: dict = {Stat.NONE: 0},
                 description: str = "Generic item",
                 value: int = 0):
        super().__init__(name, modifiers, description, value)
        
        self.interaction_action = interaction_action
        self.interaction_result = interaction_result
        
    def Interact(self, Player):
        
        if self.interaction_action == Interaction_Action.USE:
            None # TODO
        
        if self.interaction_action == Interaction_Action.NONE:
            print("Nothing interesting happens...")
            return
        if self.interaction_action == Interaction_Action.BURY:
            modifiers = list(self.modifiers.items())
            
            # The number of modifiers will always be at least one
            if len(modifiers) == 1:
                print(f"You bury {self.name} and gain {modifiers[0][1]} {Stat_To_String(modifiers[0][0])}.")
                Player.stats[modifiers[0][0]] += modifiers[0][1]
            else:
                print(f"You bury {self.name} and gain:")
                for mod in modifiers:
                    Player.stats[mod[0]] += mod[1]
                    print(f" -- {mod[1]} {Stat_To_String(mod[0])}")
                    
                    
        if self.interaction_result == Interaction_Result.DESTROY:
            Player.inventory.remove(self)

