from player import Player
from cards import Card
import random


def main():
    size = get_deck_size()
    cards = initiate_deck()
    player1, player2 = initiate_players(size, cards)
    game(player1, player2)


def game(player_1, player_2):
    while len(player_1.deck) >= 0 and len(player_2.deck) >= 0:
        if len(player_1.deck) == 0:
            print("Player 2 WON THE GAME!")
            break
        elif len(player_2.deck) == 0:
            print("Player 1 WON THE GAME!")
            break
        else:
            turn(player_1, player_2)


def turn(first: Player, second: Player):
    while len(first.deck) > 0 and len(second.deck) > 0:
        try:
            print(
                f'Player 1: {first}\nPlayer 2: {second}'
            )

            if first.active_card.value > second.active_card.value:
                first.is_winner(second.active_card)
                second.active_card = second.deck.pop(0)
                print('Player 1 Won!!')
            elif first.active_card.value < second.active_card.value:
                second.is_winner(first.active_card)
                first.active_card = first.deck.pop(0)
                print('player 2 Won!!')
            else:
                print('War!!')
                war_phase(first, second)
                first.active_card = first.deck.pop(0)
                second.active_card = second.deck.pop(0)
            print(f"Player1 has: {len(first.deck)} cards ")
            print(f"Player2 has: {len(second.deck)} cards ")
        except IndexError:
            break


def war_phase(player1: Player, player2: Player):
    player1_cards = []
    player2_cards = []
    while len(player1.deck) > 0 and len(player2.deck) > 0:
        try:
            player1_cards.append(player1.deck.pop(0))
            player1_cards.append(player1.deck.pop(0))
            player2_cards.append(player2.deck.pop(0))
            player2_cards.append(player2.deck.pop(0))
            if player1_cards[-1].value > player2_cards[-1].value:
                print("Player1 won the WAR!")
                player1.deck = player1.deck + player1_cards + player2_cards
                break
            elif player1_cards[-1].value < player2_cards[-1].value:
                print("Player2 won the WAR!")
                player2.deck = player2.deck + player1_cards + player2_cards
                break
            else:
                continue
        except IndexError:
            break


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
        "Ace",
    ]
    symbols = ["🂢", "🂣", "🂤", "🂥", "🂦", "🂧", "🂨", "🂩", "🂪", "🂫", "🂮", "🂭", "🂡"]
    for _ in range(4):
        for index, name in enumerate(names):
            card = Card(name=name, value=index, symbol=symbols[index])
            cards.append(card)
    random.shuffle(cards)
    for card in cards:
        print(f" {card.symbol} {card.name}")
    print(len(cards))
    return cards


def initiate_players(size, deck):
    print(f"Whole deck size: {len(deck)}")
    player1_cards = random.sample(deck, size)
    print(f"Player 1 card length: {len(player1_cards)}")
    for card in deck:
        if card in player1_cards:
            deck.remove(card)
    print(f"Remaining whole deck length: {len(deck)}")
    print(f"Player 1 card length: {len(player1_cards)}")
    player2_cards = random.sample(deck, size)
    player1 = Player(player1_cards)
    player2 = Player(player2_cards)
    players = [player1, player2]
    print("Player1 deck: ")
    for card in player1.deck:
        print(f"{card.symbol} {card.name}")
    print(f"Deck Size: {len(player1.deck)}")
    for card in player2.deck:
        print(f"{card.symbol} {card.name}")
    print(f"Deck Size: {len(player2.deck)}")
    print(f"Player1 active card: {player1}")
    print(f"Player2 active card: {player2}")
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


if __name__ == '__main__':
    main()
