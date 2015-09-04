# -*- coding: <UTF-8> -*-
from Card import *
from Player import *
import renpy.store as store
import renpy.exports as renpy

class SMGEngine(object):

    def __init__(self, players):
        self.players = players
        self.round = 1
        self.turn = 1

    def start_party(self):
        for player in self.players:
            player.shuffle_deck()
            player.draw_cards(10)


