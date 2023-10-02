from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.forward(-10)    
def turn_right():
     tim.setheading(tim.heading()-10)
def turn_left():
    tim.setheading(tim.heading()+10)
def goto_centre():
    tim.goto(0,0)
    tim.clear()
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="c",fun=goto_centre)

screen.exitonclick()