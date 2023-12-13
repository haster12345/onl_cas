from flask import Flask

app = Flask(__name__)

import random

class BlackjackGame:
    def __init__(self):
        self.deck = self.generate_deck()
        self.player_hand = []
        self.dealer_hand = []

    def generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        return deck

    def deal_initial_cards(self):
        random.shuffle(self.deck)
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card(), self.draw_card()]

    def draw_card(self):
        if not self.deck:
            self.deck = self.generate_deck()
            random.shuffle(self.deck)
        return self.deck.pop()

    def calculate_score(self, hand):
        score = sum([self.card_value(card) for card in hand])
        if 'A' in [card['rank'] for card in hand] and score > 21:
            score -= 10  # Adjust for the value of Ace
        return score

    def card_value(self, card):
        rank = card['rank']
        if rank in ['K', 'Q', 'J']:
            return 10
        elif rank == 'A':
            return 11
        else:
            return int(rank)

    def hit(self, hand):
        hand.append(self.draw_card())

    def is_blackjack(self, hand):
        return len(hand) == 2 and self.calculate_score(hand) == 21

    def is_bust(self, hand):
        return self.calculate_score(hand) > 21

def start_blackjack_game():
    game = BlackjackGame()
    game.deal_initial_cards()
    return game

if __name__ == "__main__":
    game = start_blackjack_game()
    print("Player hand:", game.player_hand)
    print("Dealer hand:", game.dealer_hand)
    print("Player score:", game.calculate_score(game.player_hand))
    print("Dealer score:", game.calculate_score(game.dealer_hand))
