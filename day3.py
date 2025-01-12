print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.") 
first = input("Left or right?\nType Right/Left: ").lower()
if first == "right":
  print("Sonic got the treasure before you, try again.")
elif first == 'left':
  print("Nice, you made it to the next level!")
  second = input("Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim accross the sea, pick one.\nType Swim/Wait: ").lower()
  if second == "swim":
    print("Unfortunately, you were eaten by a Big Great White Shark, try again.")
  elif second == "wait":
    print("Nice, you made it to the next level, you're pretty good at this!")
    print ("Welcome to:")
    third = input("Now that you've made it to Treasure Island, you can dig or search the cave. \n Type Dig/Cave: ").lower()
    if third == "dig":
      print("You've found the treasure, you win!")
    elif third == "cave":
      print("You were eaten by a bear, game over.")
