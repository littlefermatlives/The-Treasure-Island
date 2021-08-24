print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure")
a = input("You are on a crossroad. Do you want to move left or right? L or R\n")
if a == "R":
    print("You fall into a hole.")
    print("Game End")
else:
    print("You reached to a river.")
    print("Do you want to swim or wait? S or W")
    b = input()
    if b == "S":
        print("You are attached by trout.")
        print("Game End")
    else :
        print("You got the help and crossed the river safely.")
        print("You reached to a building.")
        print("The building have three gates. Red, Blue or Yellow")
        print("Which gate will you open? R, B, Y")
        c = input()
        if c == "B":
            print("You are eaten by beast.")
            print("Game Ever")
        elif c == 'R':
            print("You are bitten by snakes.")
            print("Game End")
        else:
            print("You Got the treasure!")
            print("You win.")

