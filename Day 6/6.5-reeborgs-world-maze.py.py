from shutil import move

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def find_path():
    if wall_in_front() and right_is_clear():
        turn_right()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front():
        turn_left()
    else:
        move()

while not at_goal():
    find_path()

# Angela's Solution:
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()