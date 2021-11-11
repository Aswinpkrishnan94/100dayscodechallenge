import turtle

import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=725, height=491)
screen.title("US states")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
answered_states = []

while len(answered_states) < 50:
    guess_state = screen.textinput(title=f"{len(answered_states)}/50 Guess the state:", prompt="state").title()
    states = data.state .to_list()
    if guess_state == "Exit":
        missing_states = []
        for state in states:
            if state not in answered_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess_state in states:
        answered_states.append(guess_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess_state)