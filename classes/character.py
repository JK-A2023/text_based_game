import random

class Character():
    def __init__(self, name, race, classification, room):
        self.name = name
        self.race = race
        self.classification = classification
        self.room = room
        self.level = 1
        self.inventory = []
        self.experience_current = 0
        self.experience_required = 10

    def player_position_check(self):
        player_map = self.room.grid_map
        
        for position, tile in enumerate(player_map):
            if tile == self.room.player_tile:
                return position


    def cpu_position_check(self):
        player_map = self.room.grid_map

        for position, tile in enumerate(player_map):
            if tile == self.room.cpu_tile:
                return position
            
    
    def get_player_row(self):
        player_position = self.player_position_check()
        if player_position <= 7:
            return 1
        elif player_position >= 8 and player_position <= 15:
            return 2
        elif player_position >= 16 and player_position <= 23:
            return 3
        else:
            return 4
        
        
    def get_cpu_row(self):
        cpu_position = self.cpu_position_check()
        if cpu_position <= 7:
            return 1
        elif cpu_position >= 8 and cpu_position <= 15:
            return 2
        elif cpu_position >= 16 and cpu_position <= 23:
            return 3
        else:
            return 4
        

    def player_cpu_attack_distance(self):
        player_old_position = self.player_position_check()
        cpu_position = self.cpu_position_check()

        if player_old_position == cpu_position + 1 or player_old_position == cpu_position - 1 or player_old_position == cpu_position + 8 or player_old_position == cpu_position - 8:
            return True
        else:
            return False 


class Player(Character):
    def __init__(self, name, race, classification, room):
        super().__init__(name, race, classification, room)
        self.name = name
        self.race = race
        self.classification = classification
        self.room = room
        self.target = None


    def player_move_up(self):
        player_old_position = self.player_position_check()
        cpu_position = self.cpu_position_check()

        if player_old_position >= 8:
            if player_old_position - 8 == cpu_position:
                print(f"You cannot be in the same place as the CPU")
            else:
                player_new_position = player_old_position - 8
                self.room.grid_map[player_new_position] = self.room.player_tile
                self.room.grid_map[player_old_position] = self.room.floor_tile
                self.room.print_map()
                return 1
        else:
            print("You are too close to the wall")


    def player_move_down(self):
        player_old_position = self.player_position_check()
        cpu_position = self.cpu_position_check()

        if player_old_position <= (self.room.number_of_floor_tiles - 8):
            if player_old_position + 8 == cpu_position:
                print(f"You cannot be in the same place as the CPU")
            else:
                player_new_position = player_old_position + 8
                self.room.grid_map[player_new_position] = self.room.player_tile
                self.room.grid_map[player_old_position] = self.room.floor_tile
                self.room.print_map()
                return 1
        else:
            print("You are too close to the wall")

    
    def player_move_right(self):
        player_old_position = self.player_position_check()
        cpu_position = self.cpu_position_check()
        print(player_old_position)

        if player_old_position % 8 != 7:
            if player_old_position + 1 == cpu_position:
                print(f"You cannot be in the same place as the CPU")
            else:
                player_new_position = player_old_position + 1
                self.room.grid_map[player_new_position] = self.room.player_tile
                self.room.grid_map[player_old_position] = self.room.floor_tile
                self.room.print_map()
                return 1
        else:
            print("You are too close to the wall")


    def player_move_left(self):
        player_old_position = self.player_position_check()
        cpu_position = self.cpu_position_check()
        # print(player_old_position)

        if player_old_position % 8 != 0:
            if player_old_position - 1 == cpu_position:
                print(f"You cannot be in the same place as the CPU")
            else:
                player_new_position = player_old_position - 1
                self.room.grid_map[player_new_position] = self.room.player_tile
                self.room.grid_map[player_old_position] = self.room.floor_tile
                self.room.print_map()
                return 1
        else:
            print("You are too close to the wall")


    def player_move(self):
        player_move_time = True
        while player_move_time:
            print("UP, DOWN, LEFT, RIGHT, CANCEL")

            player_move_choice = input(f"Where do you want to move: ").lower()
            
            if player_move_choice == 'up':
                player_move_up = self.player_move_up()
                if player_move_up == 1:
                    return player_move_up
                else:
                    continue
            elif player_move_choice == 'down':
                player_move_down = self.player_move_down()
                if player_move_down == 1:
                    return player_move_down
                else:
                    continue
            elif player_move_choice == 'right':
                player_move_right = self.player_move_right()
                if player_move_right == 1:
                    return player_move_right
                else:
                    continue
            elif player_move_choice == 'left':
                player_move_left = self.player_move_left()
                if player_move_left == 1:
                    return player_move_left
                else:
                    continue
            elif player_move_choice == 'cancel':
                break
            

    def all_player_options(self):
        self.choice_book = ["Stats", "Spellbook", "Spell Check", "Inventory", "Attack", "Regen", "Move", "Check Map"]

        self.choice_book_lower = []

        for choice in self.choice_book:
            self.choice_book_lower.append(choice.lower())

        player_choices = ', '.join(self.choice_book)
        print(f"\nChoose from the following options: \n{player_choices}")


    def display_all_options_to_player(self):
        self.all_player_options()
        player_choices = self.choice_book_lower

        player_choice = input()

        if player_choice.lower() in player_choices:
            return player_choice.lower()
        else:
            print(f"{player_choice} is not an option available: ")


    def player_option_execution(self):
        player_option = self.display_all_options_to_player()
        if player_option == 'stats':
            self.print_stats()
        elif player_option == 'spellbook':
            self.print_spellbook()
        elif player_option == 'spell check':
            self.print_spell()
        elif player_option == 'inventory':
            inv_open = True
            while inv_open:
                self.check_inventory()
                player_choice = input("Would you like to use an item? (If none, type n)")
                if player_choice != 'n':
                    return self.use_item()
                else:
                    break
        elif player_option == 'attack':
            player_row = self.get_player_row()
            cpu_row = self.get_cpu_row()
            attack_distance = self.player_cpu_attack_distance()
            if player_row != cpu_row or attack_distance != True:
                print("You are not close enough to attack")
            else:
                attack_option = input(f"Which attack would you like to use:\n{self.classification.melee_name}, {self.classification.ability_one_name}, {self.classification.ability_two_name}\n ").lower()
                if attack_option == self.classification.melee_name.lower():
                    return self.melee_attack_target()
                elif attack_option == self.classification.ability_one_name.lower():
                    return self.spell_attack(self.classification.ability_one_name)
                elif attack_option == self.classification.ability_two_name.lower():
                    return self.spell_attack(self.classification.ability_two_name)
        elif player_option == 'regen':
            return self.resource_regeneration()
        elif player_option == 'move':
            movement = self.player_move()
            return movement
        elif player_option == 'check map':
            return self.room.print_map()  


    def print_stats(self):
        print(f"\n{self.name} is a level {self.level} {self.race.race_name} {self.classification.classification_name}.")
        if self.classification.health_current == self.classification.health_maximum:
            print(f"They have {self.classification.health_current} health.")
        else:
            print(f"They have {self.classification.health_current} health, with a maximum of {self.classification.health_maximum}.")
        if self.classification.resource_amount == self.classification.resource_max:
            print(f"They have {self.classification.resource_amount} {self.classification.resource_name}.")
        else:
            print(f"They have {self.classification.resource_amount} {self.classification.resource_name}, with a maximum of {self.classification.resource_max}.")
        print(f"They have the following {self.race.race_name} racial ability:")
        self.race.print_racial_ability()
        

    def print_spellbook(self):
        player_spells = ', '.join(self.classification.spellbook)
        print(f"\n{self.name} has three abilities: ")
        print(player_spells)


    def print_spell(self):       
        user_spell_request = input("\nWhich spell do you want to see: ")
        if user_spell_request.lower() == self.classification.spellbook[0].lower():
            print(f"The {self.classification.melee_name} spell does {self.classification.melee_damage_base} damage")
        elif user_spell_request.lower() == self.classification.spellbook[1].lower():
            print(f"The {self.classification.ability_one_name} spell does {self.classification.ability_one_damage} damage, and costs {self.classification.ability_one_cost} {self.classification.resource_name}. It inflicts the target with the '{self.classification.ability_one_effect}' effect, with the following description: \n '{self.classification.ability_one_effect_description}'")
        elif user_spell_request.lower()  == self.classification.spellbook[2].lower() :
            print(f"The {self.classification.ability_two_name} spell does {self.classification.ability_two_damage} damage, and costs {self.classification.ability_two_cost} {self.classification.resource_name}. It inflicts the target with the '{self.classification.ability_two_effect}' effect, with the following description: \n '{self.classification.ability_two_effect_description}'\n")
        else:
            print(f"{self.name} does not have the {user_spell_request} ability")


    def check_inventory(self):
        item_counts = {}

        for item in self.inventory:
            if item.name in item_counts:
                item_counts[item.name] += 1
            else:
                item_counts[item.name] = 1
        item_strings = []
        for item_name, count in item_counts.items():
            if count > 1:
                item_strings.append(f"{item_name} ({count})")
            else:
                item_strings.append(item_name)
        inventory_str = ', '.join(item_strings)

        print(inventory_str)


    def remove_item_from_inventory(self, item):
        for index, value in enumerate(self.inventory):
            if value == item:
                del self.inventory[index]
                break


    def use_item(self):
        item_to_use = input("What item would you like to use: ").lower()


        for item in self.inventory:
            if item_to_use == item.name.lower():
                item.use()
                self.remove_item_from_inventory(item)
                return True
            else:
                print(f"{self.name} does not have an item called '{item_to_use}'")
            # break


    def experience_gained(self, xp_from_enemy):
        if self.level <= 60:
            self.experience_current += xp_from_enemy
            if self.experience_current >= self.experience_required:
                self.level_up()


    def level_up(self):
        self.level += 1
        print(f"\n{self.name} has leveled up! {self.name} is now level {self.level}!")
        self.classification.health_maximum += 10
        self.classification.health_current = self.classification.health_maximum
        self.classification.stamina_max += 5
        self.classification.stamina_amount = self.classification.stamina_max
        if self.classification.classification_name == "Mage":
            self.classification.resource_max += 50
            self.classification.resource_amount = self.classification.resource_max
            self.classification.ability_one_damage += 3
            self.classification.ability_one_cost += 5
            self.classification.ability_two_damage += 2
            self.classification.ability_two_cost += 3
        self.experience_required = (100 * self.level * self.level)
        
        if self.experience_current >= self.experience_required:
            self.level_up()


    def resource_regeneration(self):
        if self.classification.resource_amount == self.classification.resource_max:
            print(f"\n{self.name} already has maximum {self.classification.resource_name}")
        elif self.classification.resource_amount >= self.classification.resource_max - 9:
            old_resource_amount = self.classification.resource_amount
            self.classification.resource_amount = self.classification.resource_max
            print(f"\n{self.name}'s {self.classification.resource_name} has increased from {old_resource_amount} to {self.classification.resource_amount}")
            return True
        else:
            old_resource_amount = self.classification.resource_amount
            self.classification.resource_amount += 10
            print(f"\n{self.name}'s {self.classification.resource_name} has increased from {old_resource_amount} to {self.classification.resource_amount}")
            return True


    def melee_attack_target(self):
        random_chance = random.randint(0,100)

        if random_chance > self.classification.critical_strike_chance:
            regular_damage = self.classification.melee_damage_mult
            self.target.classification.health_current -= self.classification.melee_damage_mult
            print(f"\n{self.name} hit {self.target.name} with {self.classification.melee_name} for {regular_damage} damage!")
        else:
            crit_damage = self.classification.melee_damage_mult * self.classification.critical_strike_multiplier
            self.target.classification.health_current -= crit_damage
            print(f"\nCritical hit! {self.name} hit {self.target.name} with {self.classification.melee_name} for {crit_damage} damage!")
        print(f"{self.target.name}'s health is now {self.target.classification.health_current}!")
        self.experience_gained(1)
        if self.target.classification.health_current <= 0:
            print(f"{self.target.name} has died!")
        return True


    def spell_attack(self, user_spell_choice):
        spells = {
            self.classification.spellbook[1].lower(): (self.classification.ability_one_name, self.classification.ability_one_damage, self.classification.ability_one_cost),
            self.classification.spellbook[2].lower(): (self.classification.ability_two_name, self.classification.ability_two_damage, self.classification.ability_two_cost)
        }

        spell_info = spells.get(user_spell_choice.lower())
        
        if spell_info:
            spell_name, spell_damage, spell_cost = spell_info
            if self.classification.resource_amount >= spell_cost:
                crit_number = random.randint(1, 100)
                if crit_number < self.classification.critical_strike_chance:
                    damage_mult = spell_damage * self.classification.critical_strike_multiplier
                    self.target.classification.health_current -= damage_mult
                    self.classification.resource_amount -= spell_cost
                    print(f"\nCritical hit! {self.name} hit {self.target.name} with {spell_name} for {damage_mult} damage!")
                else:
                    self.target.classification.health_current -= spell_damage
                    self.classification.resource_amount -= spell_cost
                    print(f"\n{self.name} hit {self.target.name} with {spell_name} for {spell_damage} damage!")
                print(f"{self.target.name}'s health has fallen to {self.target.classification.health_current}!")
                print(f"{self.name}'s {self.classification.resource_name} has fallen to {self.classification.resource_amount}")
                if self.target.classification.health_current <= 0:
                    print(f"{self.target.name} has died!")
                self.experience_gained(1)
                return True
            else:
                print(f"{self.name} does not have enough {self.classification.resource_name} to use {user_spell_choice}")
        else:
            print(f"{self.name} does not have '{user_spell_choice}' in their spellbook!")


    def pick_up_item(self,item):
        self.inventory.append(item)
        print(f"You have picked up a {item.name}!")


    def passive_ability(self):  
        pass


    def active_ablity(self):
        pass


    def target_cpu(self, cpu):
        self.target = cpu
        print(f"\n\n{self.target.name} has been set as the target!")


class CPU(Character):
    def __init__(self, name, race, classification, room):
        super().__init__(name, race, classification, room)
        self.name = name
        self.race = race
        self.classification = classification
        self.room = room
        self.target = None

    def target_player(self, player):
        self.target = player
        print(f"{self.target.name} has been set as {self.name}'s target!")
    

    def cpu_move_up(self):
        cpu_position = self.cpu_position_check()

        cpu_new_position = cpu_position - 8
        self.room.grid_map[cpu_new_position] = self.room.cpu_tile
        self.room.grid_map[cpu_position] = self.room.floor_tile
        return 1
    

    def cpu_move_down(self):
        cpu_position = self.cpu_position_check()

        cpu_new_position = cpu_position + 8
        self.room.grid_map[cpu_new_position] = self.room.cpu_tile
        self.room.grid_map[cpu_position] = self.room.floor_tile
        return 1
    

    def cpu_move_right(self):
        cpu_position = self.cpu_position_check()

        cpu_new_position = cpu_position + 1
        self.room.grid_map[cpu_new_position] = self.room.cpu_tile
        self.room.grid_map[cpu_position] = self.room.floor_tile
        return 1


    def cpu_move_left(self):
        cpu_position = self.cpu_position_check()

        cpu_new_position = cpu_position - 1
        self.room.grid_map[cpu_new_position] = self.room.cpu_tile
        self.room.grid_map[cpu_position] = self.room.floor_tile
        return 1
        

    def cpu_move(self):
        cpu_position = self.cpu_position_check()
        player_position = self.player_position_check()

        cpu_row = self.get_cpu_row()
        player_row = self.get_player_row()

        if cpu_row < player_row:
            print("\nThe CPU has moved down!")
            self.cpu_move_down()
            self.room.print_map()
        elif cpu_row > player_row:
            print("\nThe CPU has moved up!")
            self.cpu_move_up()
            self.room.print_map()
        elif cpu_row == player_row:
            if cpu_position < player_position - 1:
                print("\nThe CPU has moved right!")
                self.cpu_move_right()
                self.room.print_map()
            elif cpu_position > player_position + 1:
                print("\nThe CPU has moved left!")
                self.cpu_move_left()
                self.room.print_map()


    def cpu_resource_regen(self):
        self.classification.resource_amount += self.classification.resource_regen
        print(f"\n{self.name} has increased {self.classification.resource_name} by {self.classification.resource_regen}")
        print(f"{self.name}'s {self.classification.resource_name} is now {self.classification.resource_amount}")


    def cpu_ability_one_use(self):
        self.target.classification.health_current -= self.classification.ability_one_damage
        self.classification.resource_amount -= self.classification.ability_one_cost

        print(f"\n{self.name} hit {self.target.name} with {self.classification.ability_one_name} for {self.classification.ability_one_damage}!")
        print(f"{self.target.name}'s health has fallen to {self.target.classification.health_current}!")
        print(f"{self.name}'s {self.classification.resource_name} has fallen to {self.classification.resource_amount}")

    
    def cpu_ability_two_use(self):
        self.target.classification.health_current -= self.classification.ability_two_damage
        self.classification.resource_amount -= self.classification.ability_two_cost

        print(f"\n{self.name} hit {self.target.name} with {self.classification.ability_two_name} for {self.classification.ability_two_damage}!")
        print(f"{self.target.name}'s health has fallen to {self.target.classification.health_current}!")
        print(f"{self.name}'s {self.classification.resource_name} has fallen to {self.classification.resource_amount}")


    def cpu_melee_use(self):
        random_chance = random.randint(0,100)

        if random_chance > self.classification.critical_strike_chance:
            regular_damage = self.classification.melee_damage_mult
            self.target.classification.health_current -= self.classification.melee_damage_mult
            print(f"\n{self.name} hit {self.target.name} with {self.classification.melee_name} for {regular_damage} damage!")
        else:
            crit_damage = self.classification.melee_damage_mult * self.classification.critical_strike_multiplier
            self.target.classification.health_current -= crit_damage
            print(f"\nCritical hit! {self.name} hit {self.target.name} with {self.classification.melee_name} for {crit_damage} damage!")
        print(f"{self.target.name}'s health is now {self.target.classification.health_current}!")
        if self.target.classification.health_current <= 0:
            print(f"{self.target.name} has died!")
        return True


    def cpu_check_health_potion(self):
        for item in self.inventory:
            if item.name == "Health Potion":
                return True


    def cpu_health_potion(self):
        use_health_pot = self.cpu_check_health_potion()
        if use_health_pot == True:
            for item in self.inventory:
                if item.name == "Health Potion":
                    item.use()
                    self.remove_item_from_inventory(item)
        else:
            return False


    def remove_item_from_inventory(self, item):
        for index, value in enumerate(self.inventory):
            if value == item:
                del self.inventory[index]
                break


    def cpu_action_decider(self):

        potion_in_inv = self.cpu_check_health_potion()

        does_cpu_need_to_move = self.player_cpu_attack_distance()
        if does_cpu_need_to_move != True:
            self.cpu_move()
            return True
        elif potion_in_inv == True and self.classification.health_current <= self.classification.health_maximum / 2:
            self.cpu_health_potion()    
        elif self.classification.resource_amount <= self.classification.ability_two_cost:
            self.cpu_resource_regen()
        else:
            ability_chance = random.randrange(1, 100)
            if ability_chance <= 5:
                self.cpu_melee_use()
            elif ability_chance > 5 and ability_chance <= 55:
                self.cpu_ability_one_use()
            else:
                self.cpu_ability_two_use()
