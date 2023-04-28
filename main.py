import Units.player as Player_Class
import Units.enemy as Enemy_Class

import Items.item as Item
import Items.equipment as Equipment
import Items.consumable as Consumable

import combat as Combat_Handler


def main_combat_with_input():
    enemy = Enemy_Class.Enemy("Gobbe")
    
    p_name = input("What is your name, hero?\n")
    p_atk_s = int(input("How fast are you?\n"))
    player = Player_Class.Player(p_name, p_atk_s)

    Combat_Handler.Combat(player, enemy)

def main_raw():
    
    # Two temporary, poor units
    player = Player_Class.Player("Apskrutt")
    enemy = Enemy_Class.Enemy("Gobbe", health = 40)
    
    sword = Equipment.Equipment(name = "Small Sword",
                      equipment_slot = Equipment.Equipment_Slot.WEAPON,
                      modifier = {Equipment.Item_Stat_Modifier.ATTACK_POWER: 5,
                                  Equipment.Item_Stat_Modifier.ATTACK_SPEED: 3},
                      description = "A small sword that gives a slight bonus to strength",
                      value = 20)
    
    apple = Consumable.Consumbable(name = "Apple",
                                   modifiers = {Consumable.Item_Stat_Modifier.HEALTH_MAX: 20},
                                   description = "A tiny, tiny apple",
                                   value = 1)
    
    player.Add_Item_To_Inventory(sword)
    player.Equip_Equipment(sword)

    player.Add_Item_To_Inventory(apple)
    player.Use_Consumable(apple)
    
    player.Print_Character_Info()
    
    #Combat_Handler.Combat(player, enemy)


# Start the show!    
main_raw()
