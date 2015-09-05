# -*- coding: <UTF-8> -*-
from Card import *
from Player import *
from random import *
import renpy.store as store
import renpy.exports as renpy

class SMGEngine(object):

    def __init__(self, players):
        self.players = players
        self.round = 0
        self.turn = 0
        self.actor = self.players[0]
        self.message_header = "Header"
        self.message_main = "This is the message of popup message box."
        self.message_buttons = [("Ok", "any")]
        self.output = None

    def start_party(self):
        for player in self.players:
            player.shuffle_deck()
            player.draw_cards(10)

    def pop_show(self, what):
        self.message_header = what.name
        self.message_main = what.description
        self.message_buttons = what.action_buttons

    def render_input(self, inputs):
        next_location = "player_turn"
        if "play card" in inputs:
            self.output = inputs[1]
            next_location = "show_card"
        if inputs == 'pass':
            self.players[0].passed = True
            next_location = "ai_turn"
            if self.players[1].passed:
                next_location = "round_end"
        if inputs == 'show_your_role':
            self.pop_show(self.players[0].sexual_role)
            next_location = "pop_up"
        if inputs == 'show_ai_role':
            self.pop_show(self.players[1].sexual_role)
            next_location = "pop_up"
        if inputs == 'show_your_implement':
            self.pop_show(self.players[0].active_implement)
            next_location = "pop_up"
        if inputs == 'show_ai_implement':
            self.pop_show(self.players[1].active_implement)
            next_location = "pop_up"
        return next_location

    def ai_move(self):
        next_location = "pop_up"
        if self.players[1].passed:
            return "round_end"
        rndcrd = self.players[1].hand[0]
        self.pop_show(rndcrd)
        self.players[1].play_card(rndcrd, self.players[0])
        if self.players[0].passed:
            self.players[1].passed = True
        return next_location

