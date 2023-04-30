from enum import Enum

class Stat(Enum):
    LEVEL = 1
    EXPERIENCE = 2
    HEALTH_MAX = 3
    HEALTH_CUR = 4
    ATTACK_POWER = 5
    ATTACK_SPEED = 6
    NONE = 7
    
def Stat_To_String(stat: Stat):
    if stat == Stat.LEVEL:
        return "level"
    if stat == Stat.EXPERIENCE:
        return "experience"
    if stat == Stat.HEALTH_MAX:
        return "health"
    if stat == Stat.HEALTH_CUR:
        return "health"
    if stat == Stat.ATTACK_POWER:
        return "attack power"
    if stat == Stat.ATTACK_SPEED:
        return "attack speed"
    if stat == Stat.NONE:
        return "none"
    