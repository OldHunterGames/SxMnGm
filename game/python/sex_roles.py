# -*- coding: <UTF-8> -*-
from Card import *
import renpy.store as store
import renpy.exports as renpy


class SexRole(object):

    def __init__(self, role):
        self.name = "Lover"
        self.description = "Generic lover, able to make-love."
        self.action_buttons = [("Ok", "any")]


