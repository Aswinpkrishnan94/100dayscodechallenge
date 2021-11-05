from turtle import Turtle, Screen
import random

is_race = False
screen = Screen()
screen.setup(width=500, height=500)
user_choice = screen.textinput(title="Make your guess", prompt="which turtle will win?")
colors = ["red", "blue", "yellow", "green", "black", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y_pos[index])
    turtles.append(new_turtle)

if user_choice:
    is_race = True

while is_race:

    for i in turtles:
        if i.xcor() > 230:
            win_color = i.pencolor()
            is_race = False

            if win_color == user_choice:
                print(f"You've won. The winning color is {win_color}")
            else:
                print(f"You lost. The winning color is {win_color}")

        distance = random.randint(0, 10)
        i.forward(distance)

screen.exitonclick()