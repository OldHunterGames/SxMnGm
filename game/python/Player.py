# -*- coding: <UTF-8> -*-
import renpy.store as store
import renpy.exports as renpy
from decks import *
from implements import *
from sex_roles import *
from random import shuffle

class Player(object):
    def __init__(self, person, controller):
        self.controller = controller  # ai/player
        self.name = person.name
        self.sexual_role = person.sexual_role
        self.avatar = person.avatar
        self.deck = person.deck
        self.discard_pile = []
        self.hand = []
        self.table = []
        self.passed = False
        self.pleasure = 0
        self.pleasure_threshold = 10
        self.pain = 0
        self.shame = 0
        self.extasy_tokens = 0
        self.misery_tokens = 0
        self.modifiers = []
        self.implements = []
        for implement in person.implements:  # Making implements for this instant of player, from corresponding character list
            self.implements.append(Implement(implement.name, self))
        self.active_implement = self.implements[0]

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

    def choose_implement(self):
        shuffle(self.implements)
        card = self.implements.pop()
        self.active_implement = card

class Person(object):
    def __init__(self, preset):
        self.name = "OldHuntsman"
        self.avatar = "images/male/huntsman.jpg"
        self.deck = deck_man_standart[:]
        self.implements = [Implement("Male hands"), Implement("Mr.Flabby"), Implement("Male butt"), Implement("Male mouth")]
        self.sexual_role = SexRole("Lover")
        if preset == "Copyright":
            self.name = "Copyright"
            self.avatar = "images/female/copyright.jpg"
            self.implements = [Implement("Female hands"), Implement("Dry slit"), Implement("Female butt"), Implement("Female mouth"), Implement("Boobs")]
            self.deck = deck_woman_standart[:]

