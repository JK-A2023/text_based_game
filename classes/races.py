import random

class Race:
    def __init__(self, race_name, race_passive, race_active, race_attributes):
        self.race_name = race_name
        self.race_passive = race_passive
        self.race_active = race_active
        self.race_attributes = race_attributes

    def print_racial_ability(self):
        atts = self.race_attributes['attributes']
        name = ''
        increase = 0
        for key in atts.keys():
            name = key
        for value in atts.values():
            increase = value
        print(f"{name} is increased by {increase}")


class Human(Race):
    def __init__(self):
        super().__init__("Human", "Graceful", "Indomitable Will", {"attributes": {"Dodge": 10}})

class Dwarf(Race):
    def __init__(self):
        super().__init__("Dwarf", "Jewelers Eye", "Stone-Skin", {"attributes": {"Crit-chance": 20}})

class Orc(Race):
    def __init__(self):
        super().__init__("Orc", "Distilled Rage", "Third Lung", {"attributes": {"Stamina": 5}})