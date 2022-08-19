def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_and_jump():
    if wall_in_front():
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
    else:
        move()

while not at_goal():
    move_and_jump()

# Angela's Solution

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()