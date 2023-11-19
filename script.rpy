# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Thief = Character("Thief", color="#6b705c")
define Warrior = Character("Warrior", color="#D62828")
define gamemaster = Character("gamemaster")

# The game starts here.

label start:
    "This is a visual guide to the tabletop roleplaying game to help you immerse your charater into the dungeon environment"

label sprites:
    gamemaster "Lets start by picking from the two classes you can play"
label Character:

label background:

label class:
    default learned = False
    gamemaster "Select your class"
menu:
    "Thief":
        jump sneak
    "Warrior":
        jump stronk

label sneak:
    Thief "Stelf"
    show thief at left
    gamemaster "it is advised that you play a more stealthy path and avoid enemies, sneak attacks are possible if executed carefully"
    $ learned = True
    jump common

label stronk:
    Warrior "yes"
    show warrior at left
    gamemaster "it is advised that you play a more confrontational path to fight enemies head on"
    jump common

label common:
    gamemaster "roll a dice"
        

label hall:
    show bg hall
    "You stepped on a tile in the dungeon"
    "SLAM! The gate behind you shuts you in this dungeon and the only way to exit is to move forward"
    show gate at top
    "Alea iacta est"
    "the only way forward is forward"

    scene bg hall
    if learned:
        show thief at left
    else:
        show warrior at left
        

label monster:
    default win = False
    scene bg hall
    "you see a liquid solidating into a humanoid"
    show enemy at right
    "Nightmare up ahead"
menu:
    "fight as warrior":
        show warrior at left
        Warrior "W"
        gamemaster "you have passed a strength skillcheck and killed the monster"
        $ win = True 

    "evade as thief":
        show thief at left
        Thief "sneaky beaky like"
        show sneak
        gamemaster "you have passed a stealth skillcheck and sneaked pass the monster"
        $ win = True

    "stealth attack from behind as thief":
        show thief at left
        Thief "you got blood of my suit"
        gamemaster "you have passed a stealth skillcheck and killed the monster"
        $ win = True

    "fight as thief":
        show thief at left
        Thief "YOLO"
        gamemaster "you stupid"


label victory:
    scene bg hall
    if win:
        gamemaster "you have lost _hp and gained _xp"
        jump next
    else:
        gamemaster "L"
        "ratio"
        "skill issue"
        return

label next:
    
    gamemaster "you have collected a treasure"
    show frens at top
menu:
    "yes":
        show frens at left
        "locate a treasure extract point or reach the other end of the dungeon to claim the xp within"
    "no":
        scene bg hall
    
label maze:
    scene bg maze
    gamemaster "you have reached the central maze of the map"
    "there are treasures, monsters scattered in this maze"
    "the other player will also be searching for treasures and monsters"
menu:
    "thief":
        show thief at left
        "you might be able to come across secret tunnels that you can use to your advantage"
        "this area's enemies are more concentrated and difficult, meaning less possibility of stealth kill, more risk of death"
        jump combat
    "warrior":
        show warrior at left
        "this area's enemies are more concentrated and difficult, meaning more xp per kill, but also more risk of death"
        jump combat

label combat:
    menu:
        "you see a monster up ahead":
            jump pve
        "you see a player up ahead":
            jump pvp
        "you have collected a treasure":
            show frens at left
            "locate a treasure extract point or reach the other end of the dungeon to claim the xp within"
            jump combat


label pve:
   
    scene bg maze
    "you see a liquid solidating into a humanoid"
    show enemy at right
    "Nightmare up ahead"
menu:
    "fight as warrior":
        show warrior at left
        Warrior "W"
        gamemaster "you have passed a strength skillcheck and killed the monster"
        jump end

    "evade as thief":
        show thief at left
        Thief "sneaky beaky like"
        show sneak
        gamemaster "you have passed a stealth skillcheck and sneaked pass the monster"
        jump end

    "stealth attack from behind as thief":
        show thief at left
        Thief "you got blood of my suit"
        gamemaster "you have passed a stealth skillcheck and killed the monster"
        jump end

    "fight as thief":
        show thief at left
        Thief "YOLO"
        jump end

label pvp:
  
    "you see the other player ahead"
menu:
    "warrior facing you":
        show warrior at right
        show thief at left
        Thief "i still have time to run"
        jump run
    "warrior facing away from you":
        show warrior at right
        show thief at left
        Thief "i might be able to stealth kill"
        show assassinate
        jump end
    "thief facing you":
        show warrior at left
        show thief at right
        Warrior "come closer"
        jump end
    "thief facing away from you":
        show warrior at left
        show thief at right
        Warrior "by the time i'm heard i will be close enough to strike"
        jump end

label run:
    "do you see a hidden tunnel or a corner you could turn to?"
    menu:
        "yes":
            gamemaster "you successfully hide from the player"
            show sneak
            jump aftermaze
        "no":
            gamemaster "your journey ends here"
            return

label end:
menu:
    "victory":
        gamemaster "you have killed oppositions and took all their xp and treasure boxes and skill points"
        gamemaster "you have lost _hp and gained _xp"
        jump aftermaze
    "defeat":
        gamemaster "L"
        "ratio"
        "skill issue"
        return

label aftermaze:
    gamemaster "you have survived the maze"
    gamemaster "now you need to find the exit to secure the xp you have gained"
    gamemaster "the exploration is not over yet, remain vigilant"

label endfight:
    
    scene bg hall
    "you see a liquid solidating into a humanoid"
    show enemy at right
    "Nightmare up ahead"
menu:
    "fight as warrior":
        show warrior at left
        Warrior "W"
        gamemaster "you have passed a strength skillcheck and killed the monster"
        

    "evade as thief":
        show thief at left
        Thief "sneaky beaky like"
        gamemaster "you have passed a stealth skillcheck and sneaked pass the monster"
        

    "stealth attack from behind as thief":
        show thief at left
        Thief "you got blood of my suit"
        gamemaster "you have passed a stealth skillcheck and killed the monster"
       

    "fight as thief":
        show thief at left
        Thief "YOLO"
        gamemaster "you stupid"
        return

label exit:
    gamemaster "you found the exit"
    gamemaster "open your treasure boxes and count your xp to upgrade your strength, stealth, luck, health attributes"
    gamemaster "the next dungeons awaits you"

    











        








