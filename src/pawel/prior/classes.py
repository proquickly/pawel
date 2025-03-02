"""# classes

class Adventure:
    def __init__(self, name, game_name, health, score):
        self.game_name = game_name
        self.health = None
        self.score = None
        self.player_name = name

    def play(self):
        print(f"I am playing")

    @classmethod
    def build_dungeon(cls):
        health = 100
        score = 100
        player_name = "Pawel"
        game_name = "Dungeon"
        return cls(player_name, game_name, health, score)

    @classmethod
    def build_civ(cls):
        health = 50
        score = 500
        player_name = "Pawel"
        game_name = "Civilizatio"
        return cls(player_name, game_name, health, score)"""

numbers = list(range(100000000000))

for i in numbers:
    print(i)
