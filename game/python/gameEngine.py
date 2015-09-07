# -*- coding: <UTF-8> -*-
from Card import *
from Player import *
from random import *
from static import *
from implements import *
import renpy.store as store
import renpy.exports as renpy

class SMGEngine(object):
    """
    This class controls the general game flow
    """

    def __init__(self, players):
        self.players = players
        self.round = 0
        self.turn = 0
        self.mode = "love"
        self.actor = self.players[0]
        self.message_header = "Header"
        self.message_main = "This is the message of popup message box."
        self.message_buttons = [("Ok", "any")]
        self.output = None
        self.menues = {}
        self.menues["Choose player implement"] = self.choose_player_implement()

    def choose_player_implement(self):
        list_of_menu = []
        for implement in self.players[0].implements:
            list_of_menu.append((implement.name, renpy.store.Function(self.equip_implement, implement)))
        list_of_menu.append(("Confirm and go on", renpy.store.Jump("nrc")))
        return list_of_menu

    def equip_implement(self, implement):
        self.players[0].active_implement = implement
        self.implement_transformations()

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
            self.pop_show(inputs[1])
            next_location = "show_card"
        if "show card" in inputs:
            self.pop_show(inputs[1])
            next_location = "pop_up"
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
        if self.players[1].hand:
            rndcrd = self.players[1].hand[0]
            self.pop_show(rndcrd)
            self.players[1].play_card(rndcrd, self.players[0])
        if self.players[0].passed:
            self.players[1].passed = True
        return next_location

    def scoring(self, scorePlayer, scoreComputer):
        if scorePlayer < -5:
            self.players[0].misery_tokens += 1
        if scoreComputer < -5:
            self.players[1].misery_tokens += 1
        if self.mode == "competitive":
            if scoreComputer > scorePlayer:
                self.players[1].extasy_tokens += 1
            else:
                self.players[0].extasy_tokens += 1
        else:
            if scorePlayer > self.players[0].get_pleasure_threshold():
                self.players[0].extasy_tokens += 1
            if scoreComputer > self.players[1].get_pleasure_threshold():
                self.players[1].extasy_tokens += 1

    def end_is_near(self):
        if self.mode == "rape" or self.mode == "service":
            if not self.players[0].hand:
                return True
        elif not self.players[0].hand and not self.players[1].hand:
                return True
        elif self.mode == "competitive":
            if self.players[0].extasy_tokens > 1 or self.players[1].extasy_tokens > 1:
                if self.players[0].extasy_tokens != self.players[1].extasy_tokens:
                    return True
        else:
            return False

    def results(self):
        self.message_header = "GAME OVER"
        self.message_main = "ERROR. No winner confirmed."
        if self.mode == "rape":
            self.message_main = "Your total score is " + str(self.players[0].extasy_tokens - self.players[0].misery_tokens) + " and its equal to your extasy minus your misery."
        if self.mode == "service":
            self.message_main = "Your total score is " + str(self.players[1].extasy_tokens - self.players[1].misery_tokens) + " and its equal to your partners extasy minus your partners misery."
        if self.mode == "love":
            self.message_main = "Your total score is " + str(self.players[0].extasy_tokens + self.players[1].extasy_tokens - self.players[0].misery_tokens - self.players[1].misery_tokens) + " and its equal to your AND your partners extasy minus your AND your partners misery."
        if self.mode == "competitive":
            if self.players[1].extasy_tokens > self.players[0].extasy_tokens:
                self.message_main = "Your partner has 2 extasy tokens. You WIN by making her cum first!"
            else:
                self.message_main = "You have 2 extasy tokens. You LOSE by cumming first... ("

    def round_end(self):
        global result_prercalculation
        global calculated_result
        result_prercalculation(self.players[0], self.players[1])
        result_prercalculation(self.players[1], self.players[0])
        self.scoring(calculated_result(self.players[0], self.players[1]), calculated_result(self.players[1], self.players[0]))
        self.players[0].passed, self.players[1].passed = False, False
        self.players[0].discard_pile, self.players[1].discard_pile = self.players[0].table, self.players[1].table
        self.players[0].table, self.players[1].table = [], []
        self.players[0].pleasure, self.players[1].pleasure = 0, 0
        self.players[0].pain, self.players[1].pain = 0, 0
        self.players[0].shame, self.players[1].shame = 0, 0
        self.players[0].modifiers, self.players[1].modifiers = [], []

    def implement_transformations(self):
        for player in self.players:
            if player.active_implement.name == "Mr.Flabby" and player.extasy_tokens > 0:
                player.active_implement = Implement("Dick", player)
            if player.active_implement.name == "Dry slit" and player.extasy_tokens > 0:
                player.active_implement = Implement("Juicy pussy", player)


