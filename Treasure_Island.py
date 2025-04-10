print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# This is a simple text-based adventure game where the player has to make choices to find treasure.
# The game has multiple paths and outcomes based on the player's choices.
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go.")
# The player is prompted to choose a direction (left or right).
is_left = input('   Type "left" or "right"').lower()
# If the player chooses left, they encounter a lake.
if is_left == "left":    
    print("You've come to a lake. There is an island on the middle of the lake.")
    is_wait = input('type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if is_wait == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors")
        # The player is prompted to choose a door (red, yellow, or blue).
        # Based on the player's choice, different outcomes are presented.
        is_blue = input("One red, one yellow and one blue. Which color do you choose?").lower()
        # The player is congratulated for making a "good" choice.
        if is_blue == "blue":
            print("Congratulations, you've selected staying in your ordinary life. You died without accomplishing anything...")
        # This is a reference to the game "Cyberpunk 2077" and its character Johnny Silverhand.
        # The player is notified from Johnny Silverhand.
        elif is_blue == "yellow":
            print("Wake The FuckUp, Samurai. We Have a Life To Burn. You burned. Game Over.")
        # This is a reference to the movie "The Matrix" and its character Morpheus.
        # The player is congratulated for making a good choice.
        elif is_blue == "red":
            print("You've selected how deep the rabbit-holl goes.....")
        # If the player chooses an invalid option, they are prompted to try again.
        else:
            print("Try again samurai. And just enter the correct options without any spelling errors.")
    # If the player chooses to swim, they encounter a game over scenario.
    # This is a humorous take on the idea of swimming across a lake without any means of transportation.
    else:
        print("Why are you trying to swim over a lake without anything to swim? Are you stupid? You drown in the middle of the way. Game Over.")
    # If the player chooses right, they encounter a different scenario.
else:
    print("Do you think, women are always right? ")
    # I was giving comments with AI but it didn't give a prompt for the question above. HAhahahaha.
    is_no = input('Type "yes" or "no"').lower()
    # If the player chooses "no", they are given a second chance and encounter a lake.
    if is_no == "no":
        print("Me too. I give you a second chance...")
        
        # Second chance is given to the player.

        # The code below this line is very very similar to the first part of the game. So I will not explain it again.
        # In fact, it is the same code as above and I am a begginer in Python. So I don't know how to make it more efficient.
        # I will just copy and paste the code below this line.
        # I will try to make it more efficient in the future. But for now, I will just copy and paste the code below this line.
        # If you see these comments, please provide me a feedback on how to make it more efficient.
        print("You've come to a lake. There is an island on the middle of the lake.")
        is_wait = input('type "wait" to wait for a boat. Type "swim" to swim across.').lower()
        if is_wait == "wait":
            print("You arrive at the island unharmed. There is a house with 3 doors")
            is_blue = input("One red, one yellow and one blue. Which color do you choose?").lower()
            if is_blue == "blue":
                print(
                    "Congratulations, you've selected staying in your ordinary life. You died without accomplishing anything...")
            elif is_blue == "yellow":
                print("Wake The FuckUp, Samurai. We Have a Life To Burn. You burned. Game Over.")
            elif is_blue == "red":
                print("You've selected to learn how deep the rabbit-holl goes...")
            else:
                print("Try again samurai. And just enter the correct options without any spelling errors.")
        else:
            print(
                "Why are you trying to swim over a lake without anything to swim? Are you stupid? You drown in the middle of the way. Game Over.")

    # If the player chooses "yes", they are given a "humorous" game over scenario.
    elif is_no == "yes":
        print("I don't think so. Game Over...")
    # If the player chooses an invalid option, they are prompted to try again.
    else:
        print("I can't think of any sensible humor to write here right now. Just enter the correct options without any spelling errors.")