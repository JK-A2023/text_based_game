class HealthPotion:
    def __init__(self, user):
        self.name = "Health Potion"
        self.uses = 1
        self.healing_done = 10
        self.user = user


    def use(self):
        if self.uses == 1:
            if self.user.classification.health_current == self.user.classification.health_maximum:
                print(f"{self.user.name} already has maximum health!")
            elif self.user.classification.health_current <= self.user.classification.health_maximum - 10:
                self.user.classification.health_current += self.healing_done
                print(f"{self.user.name} has used {self.name}! {self.user.name}'s health has increased to {self.user.classification.health_current}")
                return True
            elif self.user.classification.health_current >= self.user.classification.health_maximum - 9:
                self.user.classification.health_current = self.user.classification.health_maximum
                print(f"{self.user.name} has used {self.name}! {self.user.name}'s health has increased to {self.user.classification.health_current}")
                return True
            self.user.classification.health_current += self.healing_done
            self.uses = 0
            self.remove_self_from_inventory()

    

        

class ManaPotion:
    def __init__(self):
        self.name = "Mana Potion"
        self.uses = 1
        self.resource_done = 10

    def use(self, player):
        if player.classification.resource_name == "Mana":
            if self.uses == 1:
                if player.classification.resource_amount == player.classification.resource_max:
                    print(f"{player.name} already has maximum {player.classification.resource_name}!")
                elif player.classification.resource_amount <= player.classification.resource_max - 10:
                    player.classification.resource_amount += self.resource_done
                    print(f"{player.name} has used {self.name}! {player.name}'s health has increased to {player.classification.resource_amount}")
                    return True
                elif player.classification.resource_amount >= player.classification.resource_max - 9:
                    player.classification.resource_amount = player.classification.resource_max
                    print(f"{player.name} has used {self.name}! {player.name}'s health has increased to {player.classification.resource_amount}")
                    return True
                player.classification.resource_amount += self.resource_done
                self.uses = 0
        else:
            print(f"{player.name} cannot use mana potions!")

class RagePotion:
    def __init__(self):
        self.name = "Rage Potion"
        self.uses = 1
        self.resource_done = 10

    def use(self, player):
        if player.classification.resource_name == "Rage":
            if self.uses == 1:
                if player.classification.resource_amount == player.classification.resource_max:
                    print(f"{player.name} already has maximum {player.classification.resource_name}!")
                elif player.classification.resource_amount <= player.classification.resource_max - 10:
                    player.classification.resource_amount += self.resource_done
                    print(f"{player.name} has used {self.name}! {player.name}'s health has increased to {player.classification.resource_amount}")
                    return True
                elif player.classification.resource_amount >= player.classification.resource_max - 9:
                    player.classification.resource_amount = player.classification.resource_max
                    print(f"{player.name} has used {self.name}! {player.name}'s health has increased to {player.classification.resource_amount}")
                    return True
                player.classification.resource_amount += self.resource_done
                self.uses = 0
        else:
            print(f"{player.name} cannot use rage potions!")