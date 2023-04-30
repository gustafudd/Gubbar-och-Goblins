from Units.unit import *
from enum import Enum

import Items.item as Item
import Items.consumable as Consumable
import Items.equipment as Equipment
import Items.other as Item_Other

class Player(Unit):
    def __init__(self,
                 name: str,
                 level: Stat.LEVEL = 1,
                 experience_cur: Stat.EXPERIENCE = 0,
                 experience_max: int = 100,
                 health: Stat.HEALTH_MAX = 100,
                 attack_power: Stat.ATTACK_POWER = 2,
                 attack_speed: Stat.ATTACK_SPEED = 0.8,
                 description:str = "A tiny adventurer",
                 inventory = [],
                 gold = 0):
         super().__init__("Player",
                          name,
                          level,
                          experience_cur,
                          health,
                          attack_power,
                          attack_speed,
                          description)
         self.experience_max = (level * level) * 100
         self.inventory = inventory
         self.gold = gold
         self.equipped = {
             Equipment_Slot.HEAD: None,
             Equipment_Slot.SHOULDERS: None,
             Equipment_Slot.CHEST: None,
             Equipment_Slot.HANDS: None,
             Equipment_Slot.WEAPON: None,
             Equipment_Slot.SHIELD: None,
             Equipment_Slot.LEGS: None,
             Equipment_Slot.FEET: None,
         }
           
           
    def Print_Character_Info(self):
        print("--- PLAYER STATS ---")
        print(f"Name: {self.name}")
        print(f"Level: {self.stats[Stat.LEVEL]}")
        print(f"Experience: [{self.stats[Stat.EXPERIENCE]}/{self.experience_max}]")
        print(f"Health: [{self.stats[Stat.HEALTH_CUR]}/{self.stats[Stat.HEALTH_MAX]}]")
        print(f"Attack Power: {self.stats[Stat.ATTACK_POWER]}")
        print(f"Attack Speed: {self.stats[Stat.ATTACK_SPEED]}")
        
        # Item Inventory
        self.Print_Inventory()
        
        # Equipped
        print("\n --- EQUIPPED ---")
        for equipped_item in self.equipped:
            if self.equipped[equipped_item] is not None:
                print(f"{equipped_item}: {self.equipped[equipped_item].name}")
            
        print(" --- --- ---")
        
    def Print_Inventory(self):
        print(" --- INVENTORY --- ")
        for item in self.inventory:
            print(f"Item: {item.name}")
         
    def Add_Item_To_Inventory(self, item: Item):
        if not isinstance(item, Item.Item):
            raise TypeError("Item must be of Item type")
        self.inventory.append(item)     
         
    def Equip_Equipment(self, equipment: Equipment.Equipment):
        if not isinstance(equipment, Equipment.Equipment):
            raise TypeError("Equipment must be of Item type")
        if not equipment in self.inventory:
            raise ValueError("Equipment not in inventory")
                
        # Equip the item and remove from inventory
        self.equipped[equipment.equipment_slot] = equipment
        self.inventory.remove(equipment)
        
        # Modify player stats
        for Modifier in equipment.modifiers:
            if Modifier == Item.Stat.HEALTH_MAX:
                self.stats[Stat.HEALTH_MAX] += equipment.modifiers[Modifier]
                self.stats[Stat.HEALTH_CUR] += equipment.modifiers[Modifier]
            if Modifier == Item.Stat.ATTACK_POWER:
                self.stats[Stat.ATTACK_POWER] += equipment.modifiers[Modifier]
            if Modifier == Item.Stat.ATTACK_SPEED:
                self.stats[Stat.ATTACK_SPEED] += equipment.modifiers[Modifier]
                
        print(f"You equipped {equipment.name}.")
            
    """ Moves equipment from EQUIPPED to INVENTORY """
    def Remove_Equipment(self, equipment: Equipment):
        self.equipment[equipment.equipment_slot] = None
        self.inventory.append(equipment)
        
        for Modifier in equipment.modifiers:
            if Modifier == Item.Item_Stat_Modifier.HEALTH_MAX:
                self.stats[Stat.HEALTH_MAX] -= equipment.modifiers[Modifier]
                self.stats[Stat.HEALTH_CUR] -= equipment.modifiers[Modifier]
            if Modifier == Item.Item_Stat_Modifier.ATTACK_POWER:
                self.stats[Stat.ATTACK_POWER] -= equipment.modifiers[Modifier]
            if Modifier == Item.Item_Stat_Modifier.ATTACK_SPEED:
                self.stats[Stat.ATTACK_SPEED] -= equipment.modifiers[Modifier]
              
    def Use_Consumable(self, consumable: Consumable):
        if not isinstance(consumable, Consumable.Consumbable):
            raise TypeError("Consumable must be of type Consumable")
        if consumable not in self.inventory:
            raise ValueError("Consumable not in inventory")
        
        for Modifier in consumable.modifiers:
            if Modifier.value == Stat.LEVEL.value:
                self.stats[Stat.LEVEL] += consumable.modifiers[Modifier]
                print(f"You consumed {consumable.name} and gained {consumable.modifiers[Modifier]} levels.")
            elif Modifier.value == Stat.EXPERIENCE.value:
                self.stats[Stat.EXPERIENCE] += consumable.modifiers[Modifier]
                print(f"You consumed {consumable.name} and gained {consumable.modifiers[Modifier]} experience.")
            elif Modifier.value == Stat.HEALTH_MAX.value:
                self.stats[Stat.HEALTH_MAX] += consumable.modifiers[Modifier]
                self.stats[Stat.HEALTH_CUR] += consumable.modifiers[Modifier]
                print(f"You consumed {consumable.name} and gained {consumable.modifiers[Modifier]} max health.")
            elif Modifier.value == Stat.HEALTH_CUR.value:
                self.stats[Stat.HEALTH_CUR] += consumable.modifiers[Modifier]
                print(f"You consumed {consumable.name} and gained {consumable.modifiers[Modifier]} health.")
            elif Modifier.value == Stat.ATTACK_POWER.value:
                self.stats[Stat.ATTACK_POWER] += consumable.modifiers[Modifier]
                print(f"You consumed {consumable.name} and gained {consumable.modifiers[Modifier]} attack power.")
            elif Modifier.value == Stat.ATTACK_SPEED.value:
                self.stats[Stat.ATTACK_SPEED] += consumable.modifiers[Modifier]
                print(f"You consumed {consumable.name} and gained {consumable.modifiers[Modifier]} attack speed.")
            else:
                print("No modifier changed")

        self.inventory.remove(consumable)
       
    def Interact_With_Other_Item(self, item: Item_Other):
        item.Interact(self)



class Equipment_Slot(Enum):
    HEAD = 1
    SHOULDERS = 2
    CHEST = 3
    HANDS = 4
    WEAPON = 5
    SHIELD = 6
    LEGS = 7
    FEET = 8