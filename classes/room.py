import random

class Room():
    def __init__(self, player, cpu):
        self.player = player
        self.player_tile = 'P'

        self.cpu = cpu
        self.cpu_tile = 'C'
        
        self.floor_tile = 'x'
        self.room_size_options = [24, 32, 40]
        self.number_of_floor_tiles = random.choice(self.room_size_options)


    def generate_map(self):
        grid_map = []

        for _ in range(self.number_of_floor_tiles):
            grid_map.append(self.floor_tile)

        self.grid_map = grid_map


    def print_map(self):
        rows = int(self.number_of_floor_tiles / 8)
        for i in range(rows):
            start_index = i * 8
            end_index = start_index + 8
            row = self.grid_map[start_index:end_index]
            print(" ".join(map(str, row)))


    def instaniate_player(self):
        random_player_location = random.randrange(0, self.number_of_floor_tiles)
        self.grid_map[random_player_location] = self.player_tile
        self.player_position = random_player_location
        self.player_name = self.player.name


    def instaniate_cpu(self):
        random_cpu_location = random.randrange(0, self.number_of_floor_tiles)

        if random_cpu_location == self.player_position:
            self.instaniate_cpu()
        else:
            self.grid_map[random_cpu_location] = self.cpu_tile
            self.cpu_position = random_cpu_location

        self.cpu_name = self.cpu.name


    



