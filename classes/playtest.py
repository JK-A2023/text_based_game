from character import Character, Player, CPU
from classes import Classification, Warrior, Mage
from races import Race, Human, Dwarf, Orc
from items import HealthPotion, ManaPotion, RagePotion
from room import Room
import game

newRoom = Room(None, None)

newWarrior = Warrior()
newMage = Mage()

healthPot = HealthPotion()
manaPot = ManaPotion()
ragePot = RagePotion()

humanInstance = Human()
dwarfInstance = Dwarf()
orcInstance = Orc()

newChar = Player("Bonger", humanInstance, newWarrior, newRoom)
secondNewChar = CPU("Second", dwarfInstance, newMage, newRoom)

# newRoom.player = newChar
# newRoom.cpu = secondNewChar

# newRoom.generate_map()
# newRoom.instaniate_player()
# newRoom.instaniate_cpu()
# newRoom.print_map()

# newChar.print_stats()
# newChar.pick_up_item(healthPot)