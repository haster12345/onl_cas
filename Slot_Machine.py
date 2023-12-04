import random


class SlotMachine:

    def __init__(self, n):
        self.list_of_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']
        self.number_of_symbols = n

    def symbol_picker(self) -> list:
        symbol_list = []
        for i in range(self.number_of_symbols):
            symbol = random.choice(self.list_of_cards)
            symbol_list.append(symbol)

        return symbol_list
