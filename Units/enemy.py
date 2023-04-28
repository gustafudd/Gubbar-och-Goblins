from Units.unit import *
import Items.item as Item

class Enemy(Unit):
        def __init__(self, 
                     name = "Unnamed enemy",
                     level = 1,
                     experience = 10,
                     health = 10,
                     attack_power = 2,
                     attack_speed = 0.5,
                     description = "A standard enemy"):
         super().__init__("Fiend",
                          name,
                          level,
                          experience,
                          health,
                          attack_power,
                          attack_speed,
                          description)
