from enum import Enum
from stat_class import Stat

class Type(Enum):
    PLAYER = 1
    FIEND = 2
    NEUTRAL = 3
    FRIENDLY = 4

class Unit:
    def __init__(
        self,
        type_: Type, 
        name_: str, 
        level_: Stat.LEVEL,
        experience_: Stat.EXPERIENCE, 
        health_: Stat.HEALTH_MAX,
        attack_power_: Stat.ATTACK_POWER,
        attack_speed_: Stat.ATTACK_SPEED, 
        description_: str = "A simple unit"):
        
        self.type = type_
        self.name = name_
        self.stats = {
            Stat.LEVEL: level_,
            Stat.EXPERIENCE: experience_,
            Stat.HEALTH_MAX: health_,
            Stat.HEALTH_CUR: health_,
            Stat.ATTACK_POWER: attack_power_,
            Stat.ATTACK_SPEED: attack_speed_,
        }
        self.description = description_
        
    def Print_Unit_Info(self):
        print(f"Type: {self.type}")
        print(f"Name: {self.name}")
        print(f"Level: {self.stats[Stat.LEVEL]}")
        print(f"Health: {self.stats[Stat.HEALTH_CUR]}")
        print(f"Attack Power: {self.stats[Stat.ATTACK_POWER]}")
        print(f"Attack Speed: {self.stats[Stat.ATTACK_SPEED]}")

