import Items.item as Item
import Items.equipment as Equipment
import Items.consumable as Consumable
import Items.other as Other

# Complete, unfiltered, simple database of all items currently implemented.
# Some way of sorting items and dividing them up in more categories may be implemented later.

""" --- Equipment --- """
wooden_sword = Equipment.Equipment(
    name="Wooden Sword",
    equipment_slot=Equipment.Equipment_Slot.WEAPON,
    modifier={Equipment.Stat.ATTACK_POWER: 5,
              Equipment.Stat.ATTACK_SPEED: 3},
    description="A small sword that gives a slight bonus to strength and attack speed",
    value=10)

leather_helmet = Equipment.Equipment(
    name="Leather Helmet",
    equipment_slot=Equipment.Equipment_Slot.HEAD,
    modifier={Equipment.Stat.HEALTH_MAX: 20},
    description="A small sword that gives a slight bonus to health",
    value=5)

iron_shield = Equipment.Equipment(
    name="Iron Shield",
    equipment_slot=Equipment.Equipment_Slot.SHIELD,
    modifier={Equipment.Stat.HEALTH_MAX: 50,
              Equipment.Stat.ATTACK_SPEED: -0.5},
    description="A sturdy shield that increases health and decreases attack speed slightly",
    value=100)
""" --- --- ---"""


""" --- Consumables --- """
apple = Consumable.Consumbable(
    name = "Apple",
    modifiers = {Consumable.Stat.HEALTH_MAX: 20},
    description = "A tiny, tiny apple",
    value = 1)

""" --- --- ---"""

""" --- Other --- """
bones = Other.Other(
    name = "Bones",
    interaction_action = Other.Interaction_Action.BURY,
    interaction_result = Other.Interaction_Result.DESTROY,
    modifiers = {Other.Stat.EXPERIENCE: 5},
    description = "Bones from a fallen foe",
    value = 1)

ruby_crystal = Other.Other(
    name = "Ruby Crystal",
    description= "A red, shining ruby crystal. Where did this even come from?",
    value = 500)