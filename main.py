import random
import sys

def main():
    Game.main_loop()

class Game:
    def main_loop():
        ...

class Player:
    def __init__(self, deck: list, name: str) -> None:
        self.deck = deck
        self.name = name
        self.captured = []

    def shuffle():
        ...

if __name__ == "__main__":
    main()