import turtle

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



turtle.mainloop()