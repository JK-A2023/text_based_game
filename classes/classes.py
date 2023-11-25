import random

class Classification:
    def __init__(self, classification_name, health_current, health_maximum, resource_name, resource_amount, resource_max, stamina_amount, stamina_max, spellbook, melee_name, melee_damage, ability_one_name, ability_one_damage, ability_one_effect, ability_one_effect_damage, ability_one_effect_description, ability_one_effect_length, ability_one_cost, ability_two_name, ability_two_damage, ability_two_effect, ability_two_effect_damage, ability_two_effect_description, ability_two_effect_length, ability_two_cost, critical_strike_chance, critical_strike_multiplier, class_attributes, dodge_chance):
        self.classification_name = classification_name
        
        self.health_current = health_current
        self.health_maximum = health_maximum

        self.resource_name = resource_name
        self.resource_amount = resource_amount
        self.resource_max = resource_max
        self.resource_regen = 5

        self.stamina_amount = stamina_amount
        self.stamina_max = stamina_max

        self.spellbook = spellbook

        self.melee_name = melee_name
        self.melee_damage_base = melee_damage 
        self.melee_damage_mult = self.melee_damage_base + random.randrange(5)
        
        self.ability_one_name = ability_one_name
        self.ability_one_damage = ability_one_damage
        self.ability_one_effect = ability_one_effect
        self.ability_one_effect_damage = ability_one_effect_damage
        self.ability_one_effect_description = ability_one_effect_description
        self.ability_one_effect_length = ability_one_effect_length
        self.ability_one_cost = ability_one_cost

        self.ability_two_name = ability_two_name
        self.ability_two_damage = ability_two_damage
        self.ability_two_effect = ability_two_effect
        self.ability_two_effect_damage = ability_two_effect_damage
        self.ability_two_effect_description = ability_two_effect_description
        self.ability_two_effect_length = ability_two_effect_length
        self.ability_two_cost = ability_two_cost

        self.critical_strike_chance = critical_strike_chance
        self.critical_strike_multiplier = critical_strike_multiplier

        self.class_attributes = class_attributes
        self.dodge_chance = dodge_chance


class Warrior(Classification):
    def __init__(self):
        super().__init__("Warrior", 100, 100, "Rage", 100, 100, 5, 5, ["Slash", "Charge", "Slice"], "Slash", 5, "Charge", 15, "Stun", 3, "Charge at the enemy, causing them to be stunned", 1, 25, "Slice", 10, "Bleed", 2, "Causes the target to bleed for 2 rounds", 2, 20, 7.5, 2, {"Class Attributes": {"Health": 25}}, 5)


class Mage(Classification):
    def __init__(self):
        super().__init__("Mage", 75, 75, "Mana", 50, 50, 5, 5, ["Melee", "Fireball", "Frostbolt"], "Melee", 1, "Fireball", 30, "Stun", 3, "Engulfs the enemy in flame, burning them for one round.", 1, 25, "Frostbolt", 20, "Drain", 2, "Freezes the target, draining resources from them for two rounds.", 2, 20, 4, 3, {"Class Attributes": {"Mana": 25}}, 5)