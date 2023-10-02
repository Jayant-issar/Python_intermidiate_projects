import colorgram
from turtle import Turtle, Screen
import random
timmy = Turtle()
screeen = Screen()
colours = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']
timmy.pensize(15)
y_axis = 0

for i in range(10):
    timmy.penup()
    timmy.goto(-50,y_axis)
    timmy.pendown()
    y_axis += 25
    for n in range(10):
        timmy.color(random.choice(colours))
        timmy.forward(1)
        timmy.penup()
        timmy.forward(35)
        timmy.pendown() 
screeen.exitonclick()    