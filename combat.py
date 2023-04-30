import time
import random

from Units.unit import *
from Units.player import Player
from Items.loot import Loot_Generator


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
    exp = foe.stats[Stat.EXPERIENCE]
    loot = Loot_Generator.Generate_Loot()
    
    print(f"Experience gained: {exp}")
    print(f"Loot collected:")
    for item in loot:
        print(f" -- {item.name}")
    print("\n")
    
    player.stats[Stat.EXPERIENCE] += exp
    player.inventory += loot
    
def Combat_Print_Start(unit1, unit2):
    print(f"\n\nTwo contenders enter the combat arena!")
    
    print("----------")
    print(f"-- ATTACKER --") 
    unit1.Print_Unit_Info()

    print("----------")
    print("-- DEFENDER --")
    unit2.Print_Unit_Info()
    print("----------")

def Combat_Print_Attack(attacker, defender, damage):
    if damage == 0:
        print(f"{attacker.name}s attack misses {defender.name} completely!")
    if defender.stats[Stat.HEALTH_CUR] < 0:
        print(f"{attacker.name} deals a fatal blow.")
    else:
        print(f"{attacker.name} strikes {defender.name} for {damage} damage!   --  [{defender.name} HP: {defender.stats[Stat.HEALTH_CUR]}/{defender.stats[Stat.HEALTH_MAX]}]")

def Combat_Fight_Cycle(unit1, unit2):
    # Start the combat timer
    unit1_atk_timer = 0
    unit2_atk_timer = 0
    
    while True:
        combat_timer = time.time()
        if combat_timer >= unit1_atk_timer + 3/unit1.stats[Stat.ATTACK_SPEED]:
            attack_damage = max(0, random.choice([unit1.stats[Stat.ATTACK_POWER] - 2, unit1.stats[Stat.ATTACK_POWER] + 2]))
            unit2.stats[Stat.HEALTH_CUR] -= attack_damage
            Combat_Print_Attack(unit1, unit2, attack_damage)
            unit1_atk_timer = time.time()
        if combat_timer >= unit2_atk_timer + 3/unit2.stats[Stat.ATTACK_SPEED]:
            attack_damage = max(0, random.choice([unit2.stats[Stat.ATTACK_POWER] - 1, unit2.stats[Stat.ATTACK_POWER] + 1]))
            unit1.stats[Stat.HEALTH_CUR] -= attack_damage
            Combat_Print_Attack(unit2, unit1, attack_damage)
            unit2_atk_timer = time.time()
        
        if (unit1.stats[Stat.HEALTH_CUR] <= 0):
            return unit2, unit1
        if (unit2.stats[Stat.HEALTH_CUR] <= 0):
            return unit1, unit2
    
    # This case should never happen
    return unit1, unit2

def Combat_Print_Finish(winner, loser):
    print("-- Combat Finished -- ")
    print(f"{winner.name} has defeated his foe!")
    print(f"{loser.name} is dead. Sad.\n")   