name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("""You are on a dirt road, it has come to an end and you can go left or right. 
               Which way would you like to go? """).lower()
#If the player picks left
if answer == "left":
    answer = input("""You come to a river, you can walk around it or swim across?
                   Type walk to walk around or swim to swim across:  """).lower()
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator!")
    elif answer == "walk": 
        print("You walked for many miles and ran out of water, dying and losing the game..")
    else:
        print("Not a valid option. You lose...")

#If the player picks right
elif answer == "right":
     answer = input("You come to a bridge, it looks wobbly, do you want to cross or head back? (Cross/Back) ").lower()
    
     if answer == "back":
            print("Your hesitation leaves you exposed to the elements. You lose...") 
     elif answer == "cross": 
            print("As you're crossing, a plank breaks and you lose your footing. You are able to recover and keep pushing ahead, crossing the bridge.")
     else:
        print("Not a valid option. You lose...")


elif answer == "cross":
     answer = input("You come to a fork in the road. Do you take the left path, or the right?").lower() 

     if answer == "right":
            print("You take the path to the right and find yourself winding up a thin game path. At the end, you find Enlightement and leave the universe behind.") 
     elif answer == "left": 
            print("As you're walking, halfway down the path, you fall into a pit with spikes and die.")
     else:
        print("Not a valid option. You lose...")


else:
     print("You lose the game...")

