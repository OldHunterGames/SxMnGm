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
            "In this mode your final score is equal to summ of your and your partners extasy points. One extasy point awarded for ending the round with overall pleasure of equal or more than pleasure treshold. You have unlimited rounds, but limited actions. When all actions made, the game ends and you get your final score."
            $ smg_mode = "love"
            $ player = Player(Person("OldHuntsman"), "player")
            $ ai = Player(Person("Copyright"), "ai") 
        "Rape":
            "In this mode your score is equal to your extasy points. One extasy point awarded for ending the round with overall pleasure of equal or more than pleasure treshold. You have unlimited rounds, but limited actions. When all actions made, the game ends and you get your final score."
            $ smg_mode = "rape"
            $ player = Player(Person("Sergey Volkov"), "player")
            $ ai = Player(Person("Red Hood"), "ai") 
        "Service":
            "In this mode your score is equal to extasy points of your partner, but not yours. One extasy point awarded for ending the round with overall pleasure of equal or more than pleasure treshold. You have unlimited rounds, but limited actions. When all actions made, the game ends and you get your final score."
            $ smg_mode = "service"
            $ player = Player(Person("Sex Slave"), "player")
            $ ai = Player(Person("Jack o'Nine"), "ai") 
        "Sex contest":
            "This mode is cometitive. Whoever have 2 extasy points - LOSES. One extasy point given at the rounds end to player with max overall pleasure. In the case of tie - computer player wins (and extasy point goes to you!). So you will have 2 rounds at minimum and 3 at maximum to win. Just like Mortal Kombat, but make fuck not fight."
            $ smg_mode = "competitive"
            $ player = Player(Person("Bitcher"), "player")
            $ ai = Player(Person("Mistress"), "ai") 

    python:
        # Initialising game        
        players = [player, ai]  
        game = SMGEngine(players) 
        game.start_party()
        game.mode = smg_mode
        table_status = "your_hand"
    "Let's match begin!"
    call new_round   
    
    return
    
label new_round:    
    $ game.players[1].choose_implement() 
    menu:
        "Choose player implement":      # This calls a dynamicaly constructed menu to choose an implement. See the menu screen for details
            return
label nrc:            
    $ game.round += 1
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

# This label calls pop_up screen, and waits for input to it    
label pop_up:
    hide screen play_cards
    show screen pop_up
    $ location_to_call = game.render_input(ui.interact())   
    hide screen pop_up
    show screen play_cards
    call expression location_to_call     
    return

# This label calls screen to play a card from player hand        
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
    
label round_end:
    $ game.round_end()
    hide screen show_card
    hide screen play_cards    
    show screen new_round
    $ result = ui.interact()
    hide screen new_round        
    if game.end_is_near():
        hide screen round_end  
        jump session_end
    call new_round
    return
    
label session_end:
    $ game.results()
    show screen pop_up
    $ ret = ui.interact()
    return    
    
