# -*- coding: <UTF-8> -*-
from random import shuffle
import renpy.store as store
import renpy.exports as renpy

class Card(object):
    def __init__(self, name="Unknown"):
        self.name = name
        self.value = 0
        self.directions = []
        self.complimentary = ""
        self.modifier = ""
        self.special = "do_noting"
        self.description = "Blank card"
        self.autoplay = False
        if name == "Kiss":
            self.value = 2
            self.directions = ["caress", "bliss"]
            self.description = "Gives +" + str(self.value) + " pleasure to you and your partner."
        if name == "Fondle":
            self.value = 4
            self.directions = ["caress"]
            self.description = "Gives your partner +" + str(self.value) + " pleasure."
        if name == "Lick":
            self.value = 5
            self.directions = ["caress"]
            self.description = "Gives your partner +" + str(self.value) + " pleasure."
        if name == "Massage":
            self.value = 6
            self.directions = ["caress"]
            self.description = "Gives your partner +" + str(self.value) + " pleasure."
        if name == "Suck":
            self.value = 10
            self.directions = ["caress"]
            self.description = "Gives your partner +" + str(self.value) + " pleasure."
        if name == "Gentle penetration":
            self.value = 4
            self.directions = ["caress", "bliss"]
            self.description = "Gives +" + str(self.value) + " pleasure to you and your partner."
        if name == "Forceful penetration":
            self.value = 6
            self.directions = ["torture", "bliss"]
            self.description = "Gives +" + str(self.value) + " pleasure to you and pain to your partner."
        if name == "Sloppy sounds":
            self.value = 3
            self.directions = ["bliss", "disgrace"]
            self.description = "Gives you +" + str(self.value) + " pleasure and shame."
        if name == "Jerk":
            self.value = 5
            self.directions = ["bliss", "disgrace"]
            self.description = "Gives you +" + str(self.value) + " pleasure and shame."
        if name == "Bite":
            self.value = 5
            self.directions = ["torture"]
            self.description = "Gives your partner +" + str(self.value) + " pain."
        if name == "Scratch":
            self.value = 3
            self.directions = ["torture"]
            self.description = "Gives your partner +" + str(self.value) + " pain."
        if name == "Slap":
            self.value = 6
            self.directions = ["torture"]
            self.description = "Gives your partner +" + str(self.value) + " pain."
        if name == "Pinch":
            self.value = 4
            self.directions = ["torture"]
            self.description = "Gives your partner +" + str(self.value) + " pain."
        if name == "Dirty-talk":
            self.value = 3
            self.directions = ["abuse"]
            self.description = "Gives your partner +" + str(self.value) + " shame."
        if name == "Passiveness":
            self.value = 3
            self.directions = ["disgrace"]
            self.description = "Gives you +" + str(self.value) + " shame."

        if name == "Doggy-style":
            self.value = 4
            self.directions = ["caress", "bliss"]
            self.complimentary = "From behind"
            self.description = "Gives +" + str(self.value) + " pleasure to you and your partner. Doubled if partner have 'From behind' active."
        if name == "From behind":
            self.value = 2
            self.directions = ["caress", "bliss"]
            self.complimentary = "Doggy-style"
            self.description = "Gives +" + str(self.value) + " pleasure to you and your partner. Doubled if partner have 'Doggy-style' active."
        if name == "On top":
            self.value = 4
            self.directions = ["caress", "bliss"]
            self.complimentary = "Under"
            self.description = "Gives +" + str(self.value) + " pleasure to you and your partner. Doubled if partner have 'Under' active."
        if name == "Under":
            self.value = 2
            self.directions = ["caress", "bliss"]
            self.complimentary = "On top"
            self.description = "Gives +" + str(self.value) + " pleasure to you and your partner. Doubled if partner have 'On top' active."
        if name == "Side pose":
            self.value = 3
            self.directions = ["caress", "bliss"]
            self.complimentary = "Side pose"
            self.description = "Gives +" + str(self.value) + " pleasure to you and your partner. Doubled if partner also have 'Side pose' active."
        if name == "Sixty-nine":
            self.value = 4
            self.directions = ["caress", "bliss"]
            self.complimentary = "Sixty-nine"
            self.description = "Gives +" + str(self.value) + " pleasure to you and your partner. Doubled if partner also have 'Side pose' active."

        if name == "Age-play":
            self.special = "fetish"
            self.value = 2
            self.directions = ["disgrace", "shame"]
            self.description = "Gives you and your partner +" + str(self.value) + " shame. You gain new action from your inactive potential."
        if name == "Foot worship":
            self.special = "fetish"
            self.value = 4
            self.directions = ["caress", "shame"]
            self.description = "Gives your partner +" + str(self.value) + " pleasure and equal shame to you. You gain new action from your inactive potential."
        if name == "Golden shower":
            self.special = "fetish"
            self.value = 6
            self.directions = ["disgrace"]
            self.description = "Gives your partner +" + str(self.value) + " shame. You gain new action from your inactive potential."

        if name == "Command":
            self.special = "command"
            self.description = "If your partners pleasure is less than shame and pain, disregard one of your partners actions with persistent effect."
        if name == "Guidance":
            self.special = "guidance"
            self.description = "If your partners pleasure is more than shame and pain, disregard one of your partners actions with persistent effect."
        if name == "Harmony":
            self.special = "harmony"
            self.description = "If your partners pleasure is more than shame and pain, disregard one of your partners actions with persistent effect, and also one of your own."
        if name == "Cool down":
            self.special = "cooldown"
            self.description = "If you have no shame or pain, disregard one of your actions with persistent effect."
        if name == "Frenzy":
            self.special = "frenzy"
            self.description = "Make two random actions from your inactive potential."
        if name == "Improvisation":
            self.special = "improvisation"
            self.description = "Chose one action from your inactive potential and make it immediately."
        if name == "Repeating":
            self.special = "repeating"
            self.description = "Chose one action from your past actions and make it again immediately."

        if name == "Soft maso":
            self.modifier = "soft_maso"
            self.description = "At the end of round, if your pain is less than your pleasure, all your pain is converted to pleasure."
        if name == "Black maso":
            self.modifier = "black_maso"
            self.description = "At the end of round. all your pain is converted to pleasure."
        if name == "Psi-maso":
            self.modifier = "psi_maso"
            self.description = "At the end of round, all your shame is converted to pleasure."
        if name == "Submission":
            self.modifier = "submission"
            self.description = "At the end of round, if your pain is less than your pleasure, and your shame is also less than your pleasure, all your pain and shame is converted to pleasure."
        if name == "Enslavement":
            self.modifier = "enslavement"
            self.description = "At the end of round, all your pain and shame is converted to pleasure."
        if name == "Sadism":
            self.modifier = "sadism"
            self.description = "At the end of round, your gain pleasure equal to your partners pain."
        if name == "Mockery":
            self.modifier = "mockery"
            self.description = "At the end of round, your gain pleasure equal to your partners shame."
        if name == "Dominance":
            self.modifier = "dominance"
            self.description = "At the end of round, your gain pleasure equal to your partners pain and shame."
        if name == "Passion":
            self.modifier = "passion"
            self.description = "At the end of round, your pleasure points are doubled."
        if name == "Laceration":
            self.modifier = "laceration"
            self.description = "At the end of round, your pain points are doubled."
        if name == "Hysteria":
            self.modifier = "hysteria"
            self.description = "At the end of round, your shame points are doubled."
        if name == "Tenderness":
            self.modifier = "tenderness"
            self.description = "At the end of round, your partners pleasure points are doubled."
        if name == "Brutality":
            self.modifier = "brutality"
            self.description = "At the end of round, your partners pain points are doubled."
        if name == "Cruelty":
            self.modifier = "cruelty"
            self.description = "At the end of round, your partners shame points are doubled."
        if name == "Cumshot":
            self.modifier = "cumshot"
            self.description = "At the end of round, if you have an erected dick gain an extasy point even if your pleasure is less than pleasure threshold."
        if name == "Cum together":
            self.modifier = "cum_together"
            self.description = "At the end of round, if you AND your partner both gain an extasy point - gain one bonus extasy point."
        if name == "Multiorgasm":
            self.modifier = "multiorgasm"
            self.description = "At the end of round, you gain extasy equal to pleasure divided by pleasure threshold, rounded down."
        if name == "Squirt":
            self.modifier = "squirt"
            self.description = "At the end of round, if you gain extasy point gain double your extasy point count afterwards."

    def played_on(self, target, actor):
        if self.directions:
            self.value_implementation(target, actor)
            for card in target.table:
                if card.name == self.complimentary:
                    self.value_implementation(target, actor)
        if self.modifier:
            target.modifiers.append(self.modifier)
        special_effect = getattr(self, self.special)
        special_effect(target, actor)

    def value_implementation(self, target, actor):
        for direction in self.directions:
            if direction == "caress": target.pleasure += self.value
            if direction == "bliss": actor.pleasure += self.value
            if direction == "abuse": target.shame += self.value
            if direction == "disgrace": actor.shame += self.value
            if direction == "torture": target.pain += self.value
            if direction == "suffering": actor.pleasure += self.value

    def do_noting(self, target, actor):
        pass

    def tease(self, target, actor):
        target.draw_cards(2)

    def fetish(self, target, actor):
        actor.draw_cards(1)

    def frenzy(self, target, actor):
        actor.draw_and_play(2, target)
