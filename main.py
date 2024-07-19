from player import Player
from cards import Card
import random


def main():
    size = get_deck_size()
    cards = initiate_deck()
    player1, player2 = initiate_players(size, cards)


def initiate_deck():
    cards = []
    names = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "ace",
    ]
    symbols = ["🂢", "🂣", "🂤", "🂥", "🂦", "🂧", "🂨", "🂩", "🂪", "🂫", "🂮", "🂭", "🂡"]
    for _ in range(4):
        for index, name in enumerate(names):
            card = Card(name=name, value=index, symbol=symbols[index])
            cards.append(card)
    return cards


def initiate_players(size, deck):
    remaining_deck = deck
    player1_cards = random.samble(remaining_deck, size)
    for card in remaining_deck:
        if card in player1_cards:
            remaining_deck.remove(card)
    player2_cards = random.samble(remaining_deck, size)
    player1 = Player(player1_cards)
    player2 = Player(player2_cards)
    players = [player1, player2]
    return players


def get_deck_size():
    while True:
        try:
            size = int(input("Choose deck size: "))
            if size > 26 or size < 10:
                raise ValueError()
            return size
        except (TypeError, ValueError):
            print("Please type in only positive integers between 10 to 26")
            continue


initiate_deck()
