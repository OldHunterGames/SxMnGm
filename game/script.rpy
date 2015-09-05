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
    call new_turn
    return
    
label new_turn:
    $ game.turn += 1    
    call player_turn
    return

label ai_turn:
    $ location_to_call = game.ai_move()
    call expression location_to_call      
    return
    
label player_turn:
    if game.players[0].passed:
        call ai_turn
    else:
        $ location_to_call = game.render_input(ui.interact())  
        call expression location_to_call   
    return

label pop_up:
    hide screen play_cards
    show screen pop_up
    $ location_to_call = game.render_input(ui.interact())   
    hide screen pop_up
    show screen play_cards
    call expression location_to_call     
    return
    
label show_card:
    hide screen play_cards
    show screen show_card
    $ result = ui.interact()
    if result == "confirm":
        $ game.players[0].play_card(game.output, game.players[1])
        hide screen show_card
        show screen play_cards
        call ai_turn
    else:
        call player_turn
    return
    
label play_card:
    hide screen play_cards
    show screen show_card
    $ result = ui.interact()
    if result == "confirm":
        $ active_player.play_card(card, game.players[1])
        hide screen show_card
        show screen play_cards
    else:
        call player_turn
    return    
    
label test:
    "Test complete!"
    return
    
label round_end:
    $ round_end(game.players[0], game.players[1])
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
        
