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
        self.skill = "general"
        self.sensitive = False
        self.penetrator = False
        self.hole = False
        self.charged = True
        self.used = False
        self.rough = False
        self.action_buttons = [("Ok", "any")]
        if name == "Male hands":
            self.skill = "petting"
        if name == "Boobs":
            self.image = "images/implement/boobs.jpg"
            self.size = "B"
            self.skill = "petting"
            self.sensitive = True
            self.description = "Sensitive (+3 to pain and pleasure gained). Medium sized boobs add +2 to partners pleasure gains."
        if name == "Mr.Flabby":
            self.image = "images/implement/flabby.jpg"
            self.skill = "none"
            self.sensitive = True
            self.description = "Sensitive (+3 to pain and pleasure gained). If you have extasy tokens, discard Mr.Flabby and gain erected Dick (must be charged to work)! Returns to player after discard."
        if name == "Dick":
            self.image = "images/implement/dick.jpg"
            self.size = "L"
            self.skill = "penetration"
            self.erogenous = True
            self.penetrator = True
            self.description = "Size L. Sensitive (+3 to pain and pleasure gained). Penetrative (adds pleasure or pain to you and your partner with penetrative actions, depending on respective sizes of dick and hole)."
        if name == "Dry slit":
            self.image = "images/implement/dry_slit.jpg"
            self.skill = "penetration"
            self.sensitive = True
            self.hole = True
            self.rough = True
            self.description = "Sensitive (+3 to pain and pleasure gained). Rough hole - you gain pain equal to pleasure gainded with all penetrative actions. If you have extasy tokens, discard dry slit and gain juicy pussy."
        if name == "Juicy pussy":
            self.image = "images/implement/juicy_pussy.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.sensitive = True
            self.hole = True
            self.description = "Sensitive (+3 to pain and pleasure gained). Tight hole (adds pleasure or pain to you and your partner with penetrative actions, depending on respective sizes of penetrator and hole)."
        if name == "Female butt":
            self.image = "images/implement/female_butt.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.hole = True
            self.rough = True
            self.description = "Rough hole - you gain pain equal to pleasure gainded with all penetrative actions."
        if name == "Male butt":
            self.image = "images/implement/male_butt.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.hole = True
            self.rough = True
            self.description = "Rough hole - you gain pain equal to pleasure gainded with all penetrative actions."
        if name == "Female asshole":
            self.image = "images/implement/female_asshole.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.sensitive = True
            self.hole = True
        if name == "Male asshole":
            self.image = "images/implement/male_asshole.jpg"
            self.size = "Tight"
            self.skill = "penetration"
            self.sensitive = True
            self.hole = True
        if name == "Female hands":
            self.image = "images/implement/female_hand.jpg"
        if name == "Female mouth":
            self.image = "images/implement/female_mouth.jpg"
            self.size = "Slimy"
            self.skill = "oral"
            self.hole = True
            self.description = "Double value for all oral actions. Slimy hole (adds your skill to your partner pleasure gains with penetrative skills."
        if name == "Male mouth":
            self.image = "images/implement/male_mouth.jpg"
            self.size = "Slimy"
            self.skill = "oral"
            self.hole = True
            self.description = "Double value for all oral actions. Slimy hole (adds your skill to your partner pleasure gains with penetrative skills."

