class Recording:
    def __init__(self, length: int):
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("Length cannot be negative")

class Player:
    def __init__(self, name: str, player_number: int):
        self.__name = name
        self.__player_number = player_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name != "":
            self.__name = name
        else:
            raise ValueError("The name may not be an empty string")

    @property
    def player_number(self):
        return self.__player_number

    @player_number.setter
    def player_number(self, player_number: int):
        if player_number > 0:
            self.__player_number = player_number
        else:
            raise ValueError("The player number must be a positive integer")

if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)

    player = Player("Betty Ballmer", 10)
    print(player.name)
    print(player.player_number)

    player.name = "Buster Balls"
    player.player_number = 11
    print(player.name)
    print(player.player_number)