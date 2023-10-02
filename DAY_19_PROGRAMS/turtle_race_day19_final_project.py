from turtle import Turtle, Screen
import random

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
x_axis = -230
y_axis = -50

screen = Screen()
screen.listen()
screen.setup(500,400) 

user_bet = screen.textinput(title="make your bet",prompt="what is the colour of turtle you wish to fbet for ?")
print(f"your bet is on {user_bet} turtle")

turtle_names = []

for i in colours:
    tim = Turtle("turtle")
    tim.color(i)
    tim.penup()
    tim.goto(x_axis,y_axis)
    y_axis += 25
    turtle_names.append(tim)

game_running = False
if user_bet:
    game_running = True

max = 0    
while game_running:
    for i in turtle_names:
        i.forward(random.randint(1,4))
        if i.xcor() == 230:
            game_running = False

winner_index = 0

for i in turtle_names:
    if i.xcor() > max:
        max = i.xcor()
for i in turtle_names:
    if i.xcor() == max:
          winner_index += turtle_names.index(i)
          
winner = colours[winner_index]

print(f"{winner} is the winner")
if user_bet == winner:
    print("you won th ebet")
else:
    print('you lost the bet')
        
        
        
        
            
    

screen.exitonclick()