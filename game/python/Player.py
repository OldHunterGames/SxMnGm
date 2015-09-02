# -*- coding: <UTF-8> -*-
import renpy.store as store
import renpy.exports as renpy
from random import shuffle

class Player(object):
    def __init__(self, name, controller):
        self.name = name
        self.deck = []
        self.discard_pile = []
        self.hand = []
        self.table = []
        self.controller = controller  # ai/player
        self.passed = False

        self.pleasure = 0
        self.pleasure_threshold = 10
        self.pain = 0
        self.shame = 0
        self.extasy_tokens = 0
        self.misery_tokens = 0
        self.modifiers = []

    def shuffle_deck(self):
        shuffle(self.deck)

    def draw_cards(self, num=1):
        if num > len(self.deck):
            num = len(self.deck)
        for n in range(num):
            self.hand.append(self.deck.pop())

    def draw_and_play(self, num=1, target=None):
        if num > len(self.deck):
            num = len(self.deck)
        for n in range(num):
            card = self.deck.pop()
            self.table.append(card)
            card.played_on(target, self)

    def play_card(self, card, target):
        self.hand.remove(card)
        self.table.append(card)
        card.played_on(target, self)