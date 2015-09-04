init -1 python:
    import sys
    sys.path.append(renpy.loader.transfn("python"))

init python:
    from Card import *
    from Player import *
    from static import *
    from decks import *
    from implements import *
    from gameEngine import *
    import random
    from random import shuffle

# The game starts here.
label start:
    show expression "images/bg.jpg" as bg    
    
    menu:
        "Make love":
            "In this mode your final score is equal to summ of your and your partners extasy points. One extasy point awarded for ending the round with overall pleasure of 10+. You have unlimited rounds, but limited actions. When all actions made, the game ends and you get your final score."
            $ smg_mode = "love"
        "Rape":
            "In this mode your score is equal to your extasy points. One extasy point awarded for ending the round with overall pleasure of 10+. You have unlimited rounds, but limited actions. When all actions made, the game ends and you get your final score."
            $ smg_mode = "rape"
        "Service":
            "In this mode your score is equal to extasy points of your partner, but not yours. One extasy point awarded for ending the round with overall pleasure of 10+. You have unlimited rounds, but limited actions. When all actions made, the game ends and you get your final score."
            $ smg_mode = "service"
        "Sex contest":
            "This mode is cometitive. Whoever have 2 extasy points - LOSES. One extasy point given at the rounds end to player with max overall pleasure. In the case of tie - computer player wins (and extasy point goes to you!). So you will have 2 rounds at minimum and 3 at maximum to win. Just like Mortal Kombat, but make fuck not fight."
            $ smg_mode = "competitive"
            
    "Let's match begin!"
    $ index = 0
    $ table_status = "your_hand"
    call load_resources   
    
    return
    
label new_round:    
    $ game.players[0].choose_implement()    
    $ game.players[1].choose_implement()    
    show screen play_cards
    while True:
        $ active_player = players[index]
        $ index = index = (index+1) % len(players) # This is a cool python trick for working with lists :) Turn will go to the next player, we do not have to worry about a thing.
        python:
             if all(p for p in players if p.passed):
                [setattr(p, "passed", False) for p in players]
        if active_player.passed:
            $ active_player = players[index]
        if ai.passed and not player.passed:
            jump round_end
        elif active_player.controller == "ai":     
            call ai_turn
        else:
            call player_turn
    return

label ai_turn:
        if active_player.hand and not active_player.passed:
            # We let ui make a move.
            # HERE: We will make a choice between the opponents when we have more than one, just one extra line of code.
            $ card = random.choice(active_player.hand)
            $ active_player.play_card(card, player)
            "[active_player.name] action is [card.name]. [card.description]"
            if player.passed:
                $ active_player.passed = True    
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
        # Initialising players
        #p1 = Person("OldHuntsman")
        #p2 = Person("Copywrite")
        player = Player(Person("OldHuntsman"), "player")
        ai = Player(Person("Copyright"), "ai")
        players = [player, ai]        
        
        # Initialising game        
        game = SMGEngine(players) 
        game.start_party()
        
    # List with all the actors in case we get more than two in the future.
        
    call new_round    
    return
        
