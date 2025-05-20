import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie
        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            raise ValueError("Tie is unhandled")

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ["a", "e", "i", "o", "u"]
        player1_vowels = [v.lower() for v in player1_word if v in vowels]
        player2_vowels = [v.lower() for v in player2_word if v in vowels]
        if len(player1_vowels) > len(player2_vowels):
            return 1
        elif len(player1_vowels) < len(player2_vowels):
            return 2
        else:
            raise ValueError("Tie is unhandled")

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        rps_dict = {"rock paper": 2,
                    "rock scissors": 1,
                    "rock rock": None,
                    "paper rock": 1,
                    "paper scissors": 2,
                    "paper paper": None,
                    "scissors rock": 2,
                    "scissors paper": 1,
                    "scissors scissors": None}
        rps_list = ["rock", "paper", "scissors"]
        if player1_word not in rps_list:
            return 2
        elif player2_word not in rps_list:
            return 1
        elif player1_word in rps_list and player2_word in rps_list:
            return rps_dict[f"{player1_word} {player2_word}"]
        else:
            return None


p = RockPaperScissors(4)
p.play()