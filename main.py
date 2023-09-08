""" WAR: The Card Game
Pair programming project for Turing College
Just press enter to proceed through the game.
"""
import random
import sys

def main():
    """Main Game Loop"""
    game = Game()
    print(game.deck)

class Game:
    """Represents the game with all its data and related functionality"""
    def __init__(self):
        self.deck = []
        for i in range(2,15):
            self.deck.extend([Card(i, "♥"),Card(i, "♠"),Card(i, "♦"),Card(i, "♣")])

class Player:
    """Represents the players with all their data and related functionality"""
    def __init__(self, deck: list, name: str) -> None:
        self.deck = deck
        self.name = name
        self.captured = []

    def shuffle(self):
        ...

class Card:
    """Represents each card. Can be compared values directly by comparing objects.
    Prints out in a user readable format.
    """
    cards = {11: "J", 12: "Q", 13:"K", 14: "A"}
    for low_cards in range(2,11):
        cards[low_cards]=str(low_cards)

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return self.cards[self.value] +" "+ self.suit

if __name__ == "__main__":
    main()
