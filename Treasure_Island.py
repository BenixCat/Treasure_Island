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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go.")
is_left = input('   Type "left" or "right"').lower()
if is_left == "left":
    print("You've come to a lake. There is an island on the middle of the lake.")
    is_wait = input('type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if is_wait == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors")
        is_blue = input("One red, one yellow and one blue. Which color do you choose?").lower()
        if is_blue == "blue":
            print("Congratulations, you've selected staying in your ordinary life. You died without accomplishing anything...")
        elif is_blue == "yellow":
            print("Wake The FuckUp, Samurai. We Have a Life To Burn. You burned. Game Over.")
        elif is_blue == "red":
            print("You've selected how deep the rabbit-holl goes.....")
        else:
            print("Try again samurai. And just enter the correct options without any spelling errors.")
    else:
        print("Why are you trying to swim over a lake without anything to swim? Are you stupid? You drown in the middle of the way. Game Over.")
else:
    print("Do you think, women are always right? ")
    is_no = input('Type "yes" or "no"').lower()
    if is_no == "no":
        print("Me too. I give you a second chance...")
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

    elif is_no == "yes":
        print("I don't think so. Game Over...")
    else:
        print("I can't think of any sensible humor to write here right now. Just enter the correct options without any spelling errors.")