# Function to make robot turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Case is considered if the robot starts at a point surrounded by no walls ( Infinite loop condition). 
while front_is_clear():
    move()
turn_left()

# To reach the final point in the maze
while not at_goal():
    if right_is_clear():  # Checking if there is a wall on the right side
        turn_right()
        move()
    elif front_is_clear():   # checking if there is a wall on the front side
        move()
    else:
        turn_left()