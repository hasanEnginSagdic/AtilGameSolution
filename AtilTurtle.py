import turtle
import random
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catching Turtle Game")
FONT = ("Arial", 30, "normal")

def scoreTurtleSetup():
    #scoreTurtle setup function
    scoreTurtle = turtle.Turtle()
    scoreTurtle.hideturtle()
    scoreTurtle.penup()
    topHeight = screen.window_height() / 2
    scoreTurtle.setpos(0,topHeight * 0.8)
    scoreTurtle.color("dark blue")
    scoreTurtle.write(arg="Score: 0", move=False, align="center", font=FONT)

topPoint = screen.window_height() / 2
belowPoint = -(screen.window_height() / 2)
rightPoint = screen.window_width() / 2
leftPoint = -(screen.window_height() / 2)
turtleList = []
def makeTurtle():
    x = random.randint(leftPoint * 0.75, rightPoint * 0.75)
    y = random.randint(belowPoint * 0.75, topPoint * 0.75)
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.goto(x, y)
    turtleList.append(t)
def setupTurtles(numberOfTurtles=20):
    i = 1
    while i <= numberOfTurtles:
        makeTurtle()
        i += 1

def hide_turtle():
    for t in turtleList:
        t.hideturtle()


turtle.tracer(0)

setupTurtles()
scoreTurtleSetup()
hide_turtle()


turtle.tracer(1)

turtle.mainloop()