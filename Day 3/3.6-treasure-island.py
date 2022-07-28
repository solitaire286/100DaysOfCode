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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('''
*******************************
*                             *
* WELCOME TO TREASURE ISLAND. *
*                             *
*******************************
''')

print("Your mission is to find the treasure. Good Luck!\n")

left_or_right = (input("A little way into your quest, you are at a crossroads. Surrounded by a dense fog, you cannot see far. Which way do you want to go? " + 'Type "left" or "right" to get going.\n')).lower()

if left_or_right == "left":
  
  wait_or_swim = (input("After walking for miles through a dead forest, you end up at a murky lake. There is an island in the middle. " + 'Type "wait" to wait for the ferryman. Type "swim" to swim across.\n')).lower()
  
  if wait_or_swim == "wait":
    doors = (input("Barely making it out alive across treacherous waters. You arrive at an eerie old hut with three doors. With the numbers I, II, and III scratched into the wood. Which will you go through?\n")).lower()
    
    if doors == "i":
      print("You walked into a cursed room! You immediately feel something stabbing in your gut. You start bleeding profusely through your mouth and nose, unable to scream or drag yourself out of the room. You die a gruesome death in a pool of your own blood...\nGame Over!")
    
    elif doors == "ii":
      print("You found the treasure. Congratulations!!!")
    
    elif doors == "iii":
      print("You walk into the room and look around for a moment... It seemed empty at first. But no, it was booby-trapped! You are impaled by a flurry of poisoned spears hurled your way... You did not survive.\nGame Over!")
  
    else:
      print("You took too long to get into the hut. The crocodile from the lake followed you ashore. It's too big and fast, and there's no where to run except back into the water. You cannot escape. You're eaten alive...\nGame Over!")
      
  elif wait_or_swim == "swim":
    print("Halfway through your swim towards the island, you are being pulled down by something powerful. You cannot swim away, you cannot fight back. It's a huge crocodile beneath the cold, dark water dragging you to your demise...\nGame Over!")

  else:
    print("You didn't take the boat and it's too late to turn back now. Its nighttime and its raining heavily. You have no shelter to stay warm and dry. Hypothermia sets in, you're struggling to breathe and you loose consciousness... You slowly freeze to death.\nGame Over!")

elif left_or_right == "right":
  print("You hear a pack of hungry wolves coming your way. You panic and start running, while looking behind and not what lies ahead. Suddenly, you are tumbling down a cliff. You hit your head on the way down and you die instantly...\nGame Over!")

else:
  print("You lingered too long at the crossroads. A pack of hungry wolves have caught up to you. Trying to fend them off, you succumb to your wounds and die a slow and painful death...\nGame Over!")