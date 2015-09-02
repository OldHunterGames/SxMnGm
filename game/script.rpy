init -1 python:
    import sys
    sys.path.append(renpy.loader.transfn("python"))

init python:
    from Card import *
    from Player import *
    from static import *
    from decks import *
    import random
    from random import shuffle

    # Our Hotel project already has a lot of imports*
    
screen play_cards():
    frame: # AI NAME
        xysize (200, 30) # A size of this frame in pixels.
        align (0.95, 0.01) # Positioning on the screen.
        has vbox spacing 10
        text ai.name 
        
    frame: # AI STATBLOCK
        xysize (200, 220) # A size of this frame in pixels.
        align (0.95, 0.95) # Positioning on the screen.
        
        # Frame by default takes fixed as it's child. Fixed layout means everything will be positioned as programmer wishes it, no forced order or anything like that. We are not going to change that.
        # We however are going to change that default to a vbox. VBox plainly means that everything in the container will be placed vertically, automatically by Ren'Py! like so:
        has vbox spacing 10 # spacing tells vbox to put 10 pixels between it's children
        
        text "Pleasure: {}".format(ai.pleasure) 
        text "Pain: {}".format(ai.pain) 
        text "Shame: {}".format(ai.shame)         
        text "\nExtasy: {}".format(ai.extasy_tokens)         
        
    imagebutton: # AI AVATAR
        align (0.95, 0.1)
        idle im.Scale("images/female/01.jpg", 200, 200)
        hover im.MatrixColor(im.Scale("images/female/01.jpg", 200, 200), im.matrix.brightness(0.05))
        action Jump("session_end")

    imagebutton: # AI AVATAR
        align (0.95, 0.5)
        idle im.Scale("images/implement/boobs.jpg", 200, 200)
        hover im.MatrixColor(im.Scale("images/implement/boobs.jpg", 200, 200), im.matrix.brightness(0.05))
        action Jump("session_end")

    frame: # PLAYER NAME
        xysize (200, 30) # A size of this frame in pixels.
        align (0.05, 0.01) # Positioning on the screen.
        has vbox spacing 10
        text player.name 
        
    imagebutton: # PLAYER AVATAR
        align (0.05, 0.1)
        idle im.Scale("images/male/01.jpg", 200, 200)
        hover im.MatrixColor(im.Scale("images/male/01.jpg", 200, 200), im.matrix.brightness(0.05))
        action Jump("session_end")

    imagebutton: # PLAYER AVATAR
        align (0.05, 0.5)
        idle im.Scale("images/implement/dick.jpg", 200, 200)
        hover im.MatrixColor(im.Scale("images/implement/dick.jpg", 200, 200), im.matrix.brightness(0.05))
        action Jump("session_end")
        
    frame: # PLAYER STATBLOCK
        xysize (200, 220) # A size of this frame in pixels.
        align (0.05, 0.95) # Positioning on the screen.       
        has vbox spacing 10
        text "Pleasure: {}".format(player.pleasure) 
        text "Pain: {}".format(player.pain) 
        text "Shame: {}".format(player.shame)     
        text "\nExtasy tokens: {}".format(player.extasy_tokens)         
        
    frame: # CONTROL MENU
        xysize (600, 200)
        align (0.5, 0.95)
        has hbox spacing 10
        
        # Player has direct control over his/her cards, so we interate over the deck and create buttons on the screen:
        hbox: # Same thing as VBox, just horizontal positioning.
            xysize (600, 200)
            box_wrap True
        vbox:
            textbutton "Your hand":
                action SetVariable(table_status, "hand")
            textbutton "Your deck":
                action SetVariable(table_status, "yes")
            textbutton "Your discard":
                action Return(["pass"])                
        vbox:
            textbutton "PASS":
                action Return(["pass"])

    frame: # TABLE MENU
        xysize (600, 420)
        align (0.5, 0.1)
        has vbox spacing 10
        if table_status == "hand":
            for card in player.hand:
                textbutton card.name:
                    action Return(["play card", card, ai]) # action is whatever we want this button to do. Return returns a list with card and ai to the loop.
        else:
            text "yay!"            
            
screen show_card():
    frame: 
        align (0.5, 0.5)                 
        has vbox spacing 10
        text card.name
        text "".join(card.description)
        hbox:
            align (0.5, 0.9)
            box_wrap True
            textbutton "Play!":
                action Return("confirm")
            textbutton "Back":
                action Return("reject")                
    
screen new_round():
    frame: 
        align (0.5, 0.5)                 
        has vbox spacing 10
        text "End of round"
        text "One who have 2 or more extasy points (while opponent has less) is LOSER."
        text "Your extasy: [player.extasy_tokens]"
        text "Oponent extasy: [ai.extasy_tokens]"
        hbox:
            align (0.5, 0.9)
            box_wrap True
            textbutton "Next round":
                action Return("continue")
            textbutton "End game":
                action Return("end")  
                
# The game starts here.
label start:
    call load_resources
    show expression "images/bg.jpg" as bg    
    "Let's match begin!"
    $ index = 0
    $ table_status = "hand"
    call new_round
    return
    
label new_round:    
    show screen play_cards
    while not ai.passed and not player.passed:
        $ active_player = players[index]
        $ index = index = (index+1) % len(players) # This is a cool python trick for working with lists :) Turn will go to the next player, we do not have to worry about a thing.
        
        if active_player.controller == "ai":
            if active_player.hand and not active_player.passed:
                # We let ui make a move.
                # HERE: We will make a choice between the opponents when we have more than one, just one extra line of code.
                $ card = random.choice(active_player.hand)
                $ active_player.play_card(card, player)
                "[active_player.name] action is [card.name]. [card.description]"
                if player.passed:
                    $ active_player.passed = True
        else:
            call player_turn
    call round_end
    return

label player_turn:
    hide screen show_card
    show screen play_cards
    if not active_player.passed:
        $ result = ui.interact() # This is a golden line in complex Ren'Py loops, you can get player input from screen with it!
        # This obviosuly assumes that a real player is to make a move and this is the part that is going to wait for the player to make one!
        # When player clicks on a card on the screen, we get a list of a card and target in the return.
        # When we will allow more than one target, target would have to be chosen on screen just like the card... (with a button)
        if result[0] == "play card":
            $ card, target = result[1], result[2] # We get the card and opponent from the list returned by the screen!
            call show_card
        if result[0] == "pass":
            "You passed!"
            $ active_player.passed = True
    else:
        pass    
    return
    
label show_card:
    hide screen play_cards
    show screen show_card
    $ result = ui.interact()
    if result == "confirm":
        $ active_player.play_card(card, target)
        hide screen show_card
        show screen play_cards
    else:
        call player_turn
    return
    
label round_end:
    $ round_end(player, ai)
    hide screen show_card
    hide screen play_cards    
    show screen new_round
    $ result = ui.interact()
    if result == "continue":
        hide screen new_round        
        call new_round
    else:
        call session_end
    return

    
label session_end:
    "Game Over"
    return    
    
label load_resources:
    
    python:
        player = Player("Jack o'Nine", "player")
        ai = Player("Sex Slave", "ai")
        player.deck = deck_man_standart[:]
        ai.deck = deck_woman_standart[:]
        player.shuffle_deck()
        ai.shuffle_deck()
        player.draw_cards(10)
        ai.draw_cards(10)
        
        players = [player, ai] # List with all the actors in case we get more than two in the future.
        
    return
        
