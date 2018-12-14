#!/usr/bin/env python
import random

class CardDeck():
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)


    @property
    def cards(self):
        return self._cards


    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()


    # getter method
    def get_dealer(self):
        return self._dealer

    def set_dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @property  # getter property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    # @dealer.deleter
    # def dealer(self):
    #     print("BYE BYE")

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({len(self)})"

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        self._cards.append(('1', 'Joker'))
        self._cards.append(('2', 'Joker'))


