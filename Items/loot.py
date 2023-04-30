import random

import Items.item_db as IDB

# Should always equal to 100. Too lazy to generate an actual mathematical function :P
LOOT_GENERIC_RATE = 99
LOOT_COMMON_RATE = 80
LOOT_UNCOMMON_RATE = 19
LOOT_RARE_RATE = 1


# TODO: Expand this into a fully fletched class.
# Tip: Use decorators such as @classmethod to imitate static class functions

class Loot_Generator():
    def __init__(self):
        None
    
    def Generate_Loot():
        rvalue = []
        
        drop_chance = random.randint(1,100)
        print(f"Drop Chance: {drop_chance}") # DEBUGGING
        
        if (drop_chance < LOOT_GENERIC_RATE):
            rvalue.append(random.choice(Loot_Generic))
        
        if (drop_chance == LOOT_RARE_RATE):
            rvalue.append(random.choice(Loot_Uncommon))
        elif (drop_chance <= LOOT_UNCOMMON_RATE):
            rvalue.append(random.choice(Loot_Uncommon))
        else:
            rvalue.append(random.choice(Loot_Common))
            
        return rvalue

# There is a 99% chance to receive a drop from this loot table
Loot_Generic = [
    IDB.bones
]

# There is a ${LOOT_COMMON_RATE}% chance to receive a drop from this loot table
Loot_Common = [
    IDB.wooden_sword,
    IDB.leather_helmet,
    IDB.apple
]

# There is a ${LOOT_UNCOMMON_RATE}% chance to receieve a drop from this loot table
Loot_Uncommon = [
    IDB.iron_shield
]

# There is a ${LOOT_RARE_RATE}% chance to receieve a drop from this loot table
Loot_Rare = [
    IDB.ruby_crystal
]
