import random
from turtle import Turtle, Screen

screen = Screen()
screen.bgpic("road.png")
screen.setup(width=700, height=500)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
y_coord = [120, 80, 40, 0, -40, -80, -120]
all_turtles = []

for i in range(7):
	race_turtle = Turtle(shape="turtle")
	race_turtle.penup()
	race_turtle.color("black", colors[i])
	race_turtle.goto(x=-330, y=y_coord[i])
	all_turtles.append(race_turtle)
	
user_bet = screen.textinput(title="Choose your turtle", prompt="""Which turtle do you want to bet on?
(red, orange, yellow, green, blue, purple, pink)""")

race_on = True
while race_on:
	
	for turtle in all_turtles:
		if turtle.xcor() > 330:
			race_on = False
			print(f"The {turtle.fillcolor()} turtle is the winner!")
			if user_bet == turtle.fillcolor():
				print("You won the bet!")
			else:
				print("You lost the bet!")
		
		random_distance = random.randint(0, 10)
		turtle.fd(random_distance)
	
screen.bye()
