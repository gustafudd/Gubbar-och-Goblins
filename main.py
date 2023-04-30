import Units.player as Player_Class
import Units.enemy as Enemy_Class

import Items.item_db as IDB
import Items.item as Item
import Items.equipment as Equipment
import Items.consumable as Consumable
import Items.other as Item_Other

import combat as Combat_Handler

def functionality_test():
        
    # Create two temporary, poor units
    player = Player_Class.Player("Apskrutt", attack_power = 100)
    enemy = Enemy_Class.Enemy("Gobbe", health = 1)
    
    # Put the two temporary units up against each other.
    # Gobbe does not stand a chance what so ever.
    Combat_Handler.Combat(player, enemy)
    
    # We surely must have looted something!
    player.Print_Inventory()
    
    # Creating a temporary, separate list from the player inventory as some 
    # elements may be deleted during the loop, breaking the for-loop.
    for item in list(player.inventory):
        if isinstance(item, Equipment.Equipment):
            player.Equip_Equipment(item)
        if isinstance(item, Consumable.Consumbable):
            player.Use_Consumable(item)
        if isinstance(item, Item_Other.Other):
            player.Interact_With_Other_Item(item)
            
    # What is our status after all of this?
    player.Print_Character_Info()

def main():
    functionality_test()

main()
