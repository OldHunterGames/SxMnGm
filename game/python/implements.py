# -*- coding: <UTF-8> -*-
from Card import *
import renpy.store as store
import renpy.exports as renpy

class Implement(object):

    def __init__(self, name, owner=None):
        self.name = name
        self.owner = owner
        self.size = "normal"
        self.image = "images/implement/male_hand.jpg"
        self.description = "Double value for all manual actions. Handy!"
        self.skill = "petting"
        self.erogenous = False
        self.penetrator = False
        self.hole = False
        self.action_buttons = [("Ok", "any")]
        if name == "Boobs":
            self.image = "images/implement/boobs.jpg"
            self.size = "B"
            self.skill = "petting"
            self.erogenous = True
        if name == "Mr.Flabby":
            self.image = "images/implement/flabby.jpg"
            self.skill = "none"
            self.erogenous = True
        if name == "Dick":
            self.image = "images/implement/dick.jpg"
            self.size = "L"
            self.skill = "penetration"
            self.erogenous = True
            self.penetrator = True
        if name == "Dry slit":
            self.image = "images/implement/dry_slit.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.erogenous = True
            self.hole = True
        if name == "Juicy pussy":
            self.image = "images/implement/juicy_pussy.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.erogenous = True
            self.hole = True
        if name == "Female butt":
            self.image = "images/implement/female_butt.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.hole = True
        if name == "Male butt":
            self.image = "images/implement/male_butt.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.hole = True
        if name == "Female asshole":
            self.image = "images/implement/female_asshole.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.erogenous = True
            self.hole = True
        if name == "Male asshole":
            self.image = "images/implement/male_asshole.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.erogenous = True
            self.hole = True
        if name == "Female hands":
            self.image = "images/implement/female_hand.jpg"
        if name == "Female mouth":
            self.image = "images/implement/female_mouth.jpg"
            self.skill = "oral"
            self.hole = True
        if name == "Male mouth":
            self.image = "images/implement/male_mouth.jpg"
            self.skill = "oral"
            self.hole = True

