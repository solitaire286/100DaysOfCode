def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Variant 1:
while not at_goal() is True:
    if wall_in_front() is True:
        jump()
    else:
        move()

# Variant 2:
while not at_goal() == True:
    if wall_in_front() == True:
        jump()
    else:
        move()

# Variant 3:
while at_goal() != True:
    if wall_in_front() == True:
        jump()
    else:
        move()

# Variant 4:
while at_goal() == False:
    if wall_in_front() == True:
        jump()
    else:
        move()