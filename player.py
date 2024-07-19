from cards import Card
class Player:
    def __init__(self, deck):
        self.active_cards = []
        self.deck = deck
        self.active_card: Card = deck.pop(0)
        
    def is_winner(self, card: Card):
        print(len(self.deck))
        self.deck += [self.active_card, card]
        print(len(self.deck))
        
        

    def __str__(self):
        return f'{self.active_card.name} {self.active_card.symbol}'
        
    
