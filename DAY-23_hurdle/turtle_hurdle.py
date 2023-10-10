import time
from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
# creating player
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.movespeed = 0.2
    
    def up(self):
        self.forward(MOVE_DISTANCE)    
        
    def restart(self):
        self.goto(STARTING_POSITION)
        self.movespeed *= 0.92
tim = Player()

screen.onkey(tim.up, "Up")

#creating cars for obstacles
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.all_cars = []
        
       
            
    def create_cars(self):
        random_chance = random.randint(1,5)
        if random_chance == 3:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(0.75,1.8)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            random_y = random.randint(-250,275)
            new_car.goto(270,random_y)
            self.all_cars.append(new_car)
        
    def move(self):
        for car in self.all_cars:
            car.forward(5)   
                    
   
class ScoreBoard(Turtle):
    def __init__(self,x,y, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.write(f"Level : {self.score}",align="center",font=("Arial", 25, "normal") ) 

    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(f"Level : {self.score}",align="center",font=("Arial", 25, "normal") )
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial", 50, "normal"))    
    
car_1 = CarManager()   
score_b = ScoreBoard(-210,250)

game_is_on = True
while game_is_on:
    time.sleep(tim.movespeed)
    screen.update()
    car_1.create_cars()
    car_1.move()
    # decting colision with the cars
    for i in car_1.all_cars:
        if i.distance(tim) < 22:
            score_b.game_over()
            game_is_on = False
    
    if tim.ycor() > 285:
        tim.restart()
        score_b.score_increase()
    
    
screen.exitonclick()