import turtle
import random
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catching Turtle Game")
FONT = ("Arial", 30, "normal")
scoreGame = 0
scoreTurtle = turtle.Turtle()
counterTurtle = turtle.Turtle()
gameOver = False
def scoreTurtleSetup():
    #scoreTurtle setup function
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
    def handleClick(e, b):
        #burada turtle'a tıklayınca bir işleme sokulabilir
        #print(e, b)
        global scoreGame
        scoreGame += 1
        scoreTurtle.clear()
        scoreTurtle.write(arg=f"Score: {scoreGame}" , move=False, align="center", font=FONT)
    t.onclick(handleClick)
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

#aşağıdaki koda gerek kalmadı çünkü random.choice diye bir şey varmış
#turtleNumber = len(turtleList)
def showTurtleRandomly():
    if gameOver == False:
        hide_turtle()
        random.choice(turtleList).showturtle()
        screen.ontimer(showTurtleRandomly, 750)

def counter(time=30):
    global gameOver
    counterTurtle.hideturtle()
    counterTurtle.penup()
    topHeight = screen.window_height() / 2
    counterTurtle.setpos(0,topHeight * 0.8 - 40)
    counterTurtle.color("dark blue")
    counterTurtle.clear()
    if time > 0:
        counterTurtle.clear()
        counterTurtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        #lambda vermem lazım yeni fonsiyon gibi düşünüyor
        screen.ontimer(lambda: counter(time - 1), 1000)
    else:
        gameOver = True
        counterTurtle.clear()
        hide_turtle()
        counterTurtle.write(arg="game over!!!", move=False, align="center", font=FONT)


turtle.tracer(0)

setupTurtles()
scoreTurtleSetup()
counter(10)
hide_turtle()
showTurtleRandomly()

turtle.tracer(1)

turtle.mainloop()