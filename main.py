import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? (purple, red, blue, yellow)"
)

colors = ["purple", "red", "blue", "yellow"]
y_positions = [-165, -125, -85, -45]

turtles = []

# Create turtles using a loop
for i in range(len(colors)):
    turtle = Turtle("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-225, y_positions[i])
    turtles.append(turtle)

is_race_on = user_bet is not None

while is_race_on:

    for turtle in turtles:

        # Check if current turtle has crossed finish line
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()

            if winner_color.lower() == user_bet.lower():
                print(f"You won! The {winner_color} turtle is the winner.")
            else:
                print(f"You lost! The {winner_color} turtle won.")

            is_race_on = False
            break

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
screen.exitonclick()
