from turtle import *

scoreTurtle = Turtle()
myScreen = scoreTurtle.getscreen()
scoreTurtle.penup()
scoreTurtle.goto(myScreen.window_width() / 2 - 200, myScreen.window_height()/2-50)
scoreTurtle.hideturtle()
score = 0

def updatescore():
	scoreTurtle.clear()
	scoreTurtle.write("Score:" + str(score), False, "left", font=("Arial", 20, "normal"))

updatescore()

myScreen.mainloop()