class game:
    def __init__(Game, Name, Size):
        Game.Name=Name
        Game.Size=Size
class player(game):
    def player(Game):
        return f'{Game.Name} is made by: '

game=game('GTAV',110)
print(f'{game.Name}\n{game.Size}')
player=player('GTAV',110)
print(f'{player.player()}ROCKSTAR GAMES.')