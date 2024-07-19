class Card:
    def __init__(self, value, symbol, name):
        self.value = value
        self.symbol = symbol
        self.name = name
    def __str__(self):
        return f'{self.name} {self.symbol}'
