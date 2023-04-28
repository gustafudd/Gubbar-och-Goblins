import time
import random
from Units.player import Player


class Combat:
    def __init__(self):
        None
        
def Combat(unit1, unit2):
    Combat_Print_Start(unit1, unit2)
    combat_winner, combat_loser = Combat_Fight_Cycle(unit1, unit2)
    Combat_Print_Finish(combat_winner, combat_loser)
    
    if (isinstance(combat_winner, Player)):
        Combat_Exp_and_Loot(combat_winner, combat_loser)
    
def Combat_Exp_and_Loot(player, foe):
    player.experience += foe.experience
    # TODO: Generate loot-table
    
    
def Combat_Print_Start(unit1, unit2):
    print(f"\n\nTwo contenders enter the combat arena!")
    
    print("----------")
    print(f"-- ATTACKER --") 
    unit1.Print_Unit_Info()

    print("----------")
    print("-- DEFENDER --")
    unit2.Print_Unit_Info()
    print("----------")

def Combat_Print_Attack(attacker, defender, damage, defender_max_hp):
    if damage == 0:
        print(f"{attacker.name} attack misses {defender.name} completely!")
    if defender.health < 0:
        print(f"{attacker.name} deals a fatal blow.")
    else:
        print(f"{attacker.name} strikes {defender.name} for {damage} damage!   --  [{defender.name} HP: {defender.health}/{defender_max_hp}]")

def Combat_Fight_Cycle(unit1, unit2):
    # Start the combat timer
    unit1_atk_timer = 0
    unit1_start_hp = unit1.health
    unit2_atk_timer = 0
    unit2_start_hp = unit2.health
    
    while True:
        combat_timer = time.time()
        if combat_timer >= unit1_atk_timer + 3/unit1.attack_speed:
            attack_damage = max(0, random.choice([unit1.attack_power - 2, unit1.attack_power + 2]))
            unit2.health -= attack_damage
            Combat_Print_Attack(unit1, unit2, attack_damage, unit2_start_hp)
            unit1_atk_timer = time.time()
        if combat_timer >= unit2_atk_timer + 3/unit2.attack_speed:
            attack_damage = max(0, random.choice([unit2.attack_power - 1, unit2.attack_power + 1]))
            unit1.health -= attack_damage
            Combat_Print_Attack(unit2, unit1, attack_damage, unit1_start_hp)
            unit2_atk_timer = time.time()
        
        if (unit1.health <= 0):
            return unit2, unit1
        if (unit2.health <= 0):
            return unit1, unit2
    
    # This case should never happen
    return unit1, unit2

def Combat_Print_Finish(winner, loser):
    print("-- Combat Finished -- ")
    print(f"{winner.name} has defeated his foe!")
    print(f"{loser.name} is dead. Sad.")   