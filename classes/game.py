import random
from character import Character, Player, CPU
from classes import Classification, Warrior, Mage
from races import Race, Human, Dwarf, Orc
from items import HealthPotion, ManaPotion, RagePotion
from room import Room


def list_all_races():
    race_names = ["Human", "Dwarf", "Orc"]
    names_str = ', '.join(race_names)
    print(names_str)
    return race_names


def choose_race(all_races):
    race_list_in_lower = []
    for race in all_races:
        race_list_in_lower.append(race.lower())

    race_selection = True
    while race_selection:
        user_race_choice = input("Choose your character race: ")
        if user_race_choice.lower() in race_list_in_lower:
            print(f"\nYou have selected {user_race_choice.capitalize()}!")
            race_selection = False
            return user_race_choice.capitalize()
        else:
            print(f"\nPlease select a valid race:")
            list_all_races()


def race_confirm(race_choice):
    while True:
        user_race_confirm = input(f"Confirm {race_choice}? (y/n) ")
        if user_race_confirm.lower() == "y":
            print(f"\nYou have confirmed {race_choice}!")
            return race_choice
        elif user_race_confirm.lower() == 'n':
            print(f"Please reselect your race: ")
            all_race_names = list_all_races()
            user_race_select = choose_race(all_race_names)
            race_confirm = user_race_select
        else:
            print("Please respond with 'y' or 'n'.")
    return race_choice


def list_all_classes():
    class_names = ["Warrior", "Mage"]
    names_str = ', '.join(class_names)
    print(names_str)
    return class_names


def choose_class(all_classes):
    class_list_in_lower = []
    for classification in all_classes:
        class_list_in_lower.append(classification.lower())

    class_selection = True
    while class_selection:
        user_class_choice = input("Choose your character class: ")
        if user_class_choice.lower() in class_list_in_lower:
            print(f"\nYou have selected {user_class_choice.capitalize()}!")
            class_selection = False
            return user_class_choice
        else:
            print(f"\n Please select a valid class: ")
            list_all_classes()


def class_confirm(class_choice):
    while True:
        user_class_confirm = input(f"Confirm {class_choice.capitalize()}? (y/n) ")
        if user_class_confirm.lower() == "y":
            print(f"\nYou have confirmed {class_choice}!")
            return class_choice.capitalize()
        elif user_class_confirm.lower() == "n":
            print(f"Please reselect your class: ")
            all_class_names = list_all_classes()
            user_class_select = choose_class(all_class_names)
            class_confirm = user_class_select
        else:
            print("Please respond with 'y' or 'n'.")
    return class_choice


def player_character_confirmation(race_choice, class_choice):
    while True:
        character_current_confirm = input(f"\nYou have currently selected a {race_choice} {class_choice}. Do you want to confirm this choice: (y/n) ")
        if character_current_confirm.lower() == 'y':
            char_list = [race_choice, class_choice]
            print(f"You have confirmed a {race_choice} {class_choice}!")
            return char_list
        elif character_current_confirm.lower() == 'n':
            all_names = list_all_races()
            race_choose = choose_race(all_names)
            race_confirmed = race_confirm(race_choose)
            all_classes = list_all_classes()
            class_choose = choose_class(all_classes)
            class_confirmed = class_confirm(class_choose)
            return player_character_confirmation(race_confirmed, class_confirmed)
        else:
            print(f"Please respond with 'y' or 'n'")
    return char_list


def player_character_name():
    character_name = input(f"\nInput a name for your character! ")
    return character_name


def player_character_name_confirm(player_name):
    while True:
        character_name_confirm = input(f"You have named your character {player_name}. Do you want to confirm this name? (y/n) ")
        if character_name_confirm == 'y':
            print(f"You have confirmed the name '{player_name}'!")
            return player_name
        elif character_name_confirm == 'n':
            player_new_name = player_character_name()
            return player_character_name_confirm(player_new_name)
        else:
            print("Please respond with 'y' or 'n'.")
    return player_name


def room_initiation():
    room_instance = Room(None, None)
    return room_instance


def player_character_initiation(race_choice, class_choice, player_name, roomInstance):

    player_name = player_name.lower()
    player_name = player_name.capitalize()

    if race_choice == 'Human':
        humanInstance = Human()
        if class_choice == "Warrior":
            warriorInstance = Warrior()
            player_character = Player(player_name, humanInstance, warriorInstance, roomInstance)
            return player_character
        elif class_choice == "Mage":
            mageInstance = Mage()
            player_character = Player(player_name, humanInstance, mageInstance, roomInstance)
            return player_character
    elif race_choice == 'Dwarf':
        humanInstance = Dwarf()
        if class_choice == "Warrior":
            warriorInstance = Warrior()
            player_character = Player(player_name, humanInstance, warriorInstance, roomInstance)
            return player_character
        elif class_choice == "Mage":
            mageInstance = Mage()
            player_character = Player(player_name, humanInstance, mageInstance, roomInstance)
            return player_character
    elif race_choice == 'Orc':
        humanInstance = Orc()
        if class_choice == "Warrior":
            warriorInstance = Warrior()
            player_character = Player(player_name, humanInstance, warriorInstance, roomInstance)
            return player_character
        elif class_choice == "Mage":
            mageInstance = Mage()
            player_character = Player(player_name, humanInstance, mageInstance, roomInstance)
            return player_character


def cpu_initiation(roomInstance):
    cpu_name_list = ["CPU-Human-Warrior", "CPU-Human-Mage", "CPU-Dwarf-Warrior", "CPU-Dwarf-Mage", "CPU-Orc-Warrior", "CPU-Orc-Mage",]

    cpu_name = random.choice(cpu_name_list)
    
    if cpu_name == "CPU-Human-Warrior":
        class_choice = Warrior() 
        race_choice = Human()
    elif cpu_name == "CPU-Human-Mage":
        class_choice = Mage()  
        race_choice = Human()
    elif cpu_name == "CPU-Dwarf-Warrior":
        class_choice = Warrior()  
        race_choice = Dwarf()
    elif cpu_name == "CPU-Dwarf-Mage":
        class_choice = Mage()  
        race_choice = Dwarf()
    elif cpu_name == "CPU-Orc-Warrior":
        class_choice = Warrior()  
        race_choice = Orc()
    elif cpu_name == "CPU-Orc-Mage":
        class_choice = Mage()  
        race_choice = Orc()
    
    cpu_instance = CPU(cpu_name, race_choice, class_choice, roomInstance)
    print(f"\nThe CPU has chosen {cpu_instance.name}!")
    return cpu_instance


def room_setup(room, player, cpu):
    room.player = player
    room.cpu = cpu

    room_instance.generate_map()
    room_instance.instaniate_player()
    room_instance.instaniate_cpu()
    print("\nHere is the map!\n")
    room_instance.print_map()

    player_health_pot = HealthPotion(player)
    player_instance.inventory.append(player_health_pot)
    player_instance.target_cpu(cpu_instance)


    cpu_health_pot = HealthPotion(cpu)
    cpu_instance.inventory.append(cpu_health_pot)
    cpu_instance.target_player(player_instance)


def first_round_decider():
    dice_roll = random.randint(1,6)
    
    if dice_roll >= 4:
        print(f"\n\nThe dice has landed on {dice_roll}! You go first!")
        return "player"
    else:
        print(f"\n\nThe dice has landed on {dice_roll}! The CPU goes first!")
        return "cpu"
    

def first_round(first):
    player_round_number = 0
    cpu_round_number = 1
    round_counter = []
    first_round = True

    while first_round:
        if first == 'player':
            print(f"\n\nYou start the first round!")
            player_move = player_instance.player_option_execution()
            if player_move == True:
                round_counter.append(player_round_number)
                return round_counter
            else:
                continue
        elif first == 'cpu':
            print(f"\n\nCPU starts the first round!")
            cpu_move = cpu_instance.cpu_action_decider()
            round_counter.append(cpu_round_number)
            return round_counter


def game_continue(counter):
    
    game_time = True
    while game_time:
        round_counter = counter
        player_round_number = 0
        cpu_round_number = 1

        while player_instance.classification.health_current > 0 and cpu_instance.classification.health_current > 0:
            
            if player_instance.classification.health_current <= 0:
                print(f"You have been defeated! {cpu_instance.name} wins!")
                break
            else:
                if round_counter[-1] == 1:
                    player_move = player_instance.player_option_execution()
                    if player_move == True:
                        round_counter.append(player_round_number)
                        
                    else:
                        continue
            if cpu_instance.classification.health_current <= 0:
                print(f"You have won! {cpu_instance.name} has been defeated!")
                break
            else:
                cpu_move = cpu_instance.cpu_action_decider()
                round_counter.append(cpu_round_number)

        game_time = False
        break




list_of_all_races = list_all_races()
player_race_choice = choose_race(list_of_all_races)
player_race_confirm = race_confirm(player_race_choice)


list_of_all_classes = list_all_classes()
player_class_choice = choose_class(list_of_all_classes)
player_class_confirm = class_confirm(player_class_choice)


player_character_confirm = player_character_confirmation(player_race_confirm, player_class_confirm)
player_name = player_character_name()
player_name_confirm = player_character_name_confirm(player_name)


room_instance = room_initiation()


player_instance = player_character_initiation(player_race_confirm, player_class_confirm, player_name_confirm, room_instance)


cpu_instance = cpu_initiation(room_instance)


room_setup(room_instance, player_instance, cpu_instance)


first_round_number = first_round_decider()

first_round = first_round(first_round_number)

game_continue = game_continue(first_round)