import random
import sys
from turtle import Turtle,Screen
is_race_on="False"
a=Turtle("turtle")
a.color("purple")
b=Turtle("turtle")
b.color("red")
c=Turtle("turtle")
c.color("blue")
d=Turtle("turtle")
d.color("yellow")
screen=Screen()
screen.setup(500,400)
a.penup()
user_bet=screen.textinput(title="make your bet",prompt="which turtle will win the race?")
a.goto(-225,-165)
b.penup()
b.goto(-225,-125)
c.penup()
c.goto(-225,-85)
d.penup()
d.goto(-225,-45)
if user_bet:
    is_race_on=True
while is_race_on:
    if a.xcor()>230 or b.xcor()>230 or c.xcor()>230 or d.xcor()>230:
        turtles=[a,b,c,d]
        winner = max(turtles, key=lambda t: t.xcor())
        winner_color = winner.pencolor()

        if winner_color == user_bet.lower():
            print("You won!")
        else:
            print(f"You lost! The winner was {winner_color}.")
        is_race_on=False

    random_distance=random.randint(0,10)
    a.forward(random_distance)
    random_distance = random.randint(0, 10)
    b.forward(random_distance)
    random_distance = random.randint(0, 10)
    c.forward(random_distance)
    random_distance = random.randint(0, 10)
    d.forward(random_distance)


screen.exitonclick()