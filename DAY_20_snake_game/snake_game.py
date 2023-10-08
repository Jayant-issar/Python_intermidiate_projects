from turtle import Turtle, Screen
import time
import random
# from food import Food

screen = Screen()
screen.bgcolor("cyan")
screen.title("Snake game")
screen.setup(width=600, height=500)
# turning off the Tracer to close the animation
screen.tracer(0)

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        start_x_axis = 0
        start_y_axis = 0
        for _ in range(3):
            segment = Turtle("square")
            segment.penup()
            segment.goto(x=start_x_axis, y=start_y_axis)
            start_x_axis -= 20
            self.snake_segments.append(segment)
    
    def extend_snake(self):
        segment = Turtle("circle")
        segment.penup()
        segment.goto(self.snake_segments[-1].xcor()-20,self.snake_segments[-1].ycor())
        self.snake_segments.append(segment)
    
    
    def move(self):
        for seg_index in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_index - 1].xcor()
            new_y = self.snake_segments[seg_index - 1].ycor()
            self.snake_segments[seg_index].goto(new_x, new_y)
        self.snake_segments[0].forward(20)

    # Define the up function to handle direction change
    def up(self):
        current_heading = self.snake_segments[0].heading()
        if current_heading != 270:  # Avoid moving down when going up
            self.snake_segments[0].setheading(90)
    def down(self):
        current_heading = self.snake_segments[0].heading()
        if current_heading != 90:
            self.snake_segments[0].setheading(270)
    def right(self):
        current_heading = self.snake_segments[0].heading()
        if current_heading != 180:
            self.snake_segments[0].setheading(0)
    def left(self):
        current_heading = self.snake_segments[0].heading()
        if current_heading != 0:
            self.snake_segments[0].setheading(180)     
   
   
class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.penup()
        self.shapesize(0.7,0.7)
        self.color("red")
        self.speed("fastest")
        food_x = random.randint(-230,230)
        food_y = random.randint(-230,230)
        self.goto(food_x,food_y)
        self.refresh()
        
    def refresh(self):
        food_x = random.randint(-230,230)
        food_y = random.randint(-230,230)
        self.goto(food_x,food_y)
        
 # score class
 
class ScoreBoard(Turtle):       
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,218)
        self.write(f"your score is: {self.score}",align="center",font=("Arial", 20, "normal") )
        
    
    def increase_score(self):
        score_board.score += 1
        self.clear()
        self.write(f"your score is: {self.score}",align="center",font=("Arial", 20, "normal") )
    
    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER ",align="center",font=("Arial", 28, "normal") )
            
           
# Create the snake
tim = Snake()
#creting food
food = Food()
#creating score board
score_board = ScoreBoard()

# Bind the direction change function to the Up arrow key
screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.right, "Right")
screen.onkey(tim.left, "Left")

# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    tim.move()
    # checking of the collison wiht the food
    score_board
    if tim.snake_segments[0].distance(food) < 15:
        score_board.increase_score()
        tim.extend_snake()
        food.refresh()
    
    if tim.snake_segments[0].xcor() > 299 or tim.snake_segments[0].xcor() < -299 or tim.snake_segments[0].ycor() > 249 or tim.snake_segments[0].ycor() < -249:
        game_is_on =False
        score_board.game_over()
    
    # checking if the tail colids with the sanke body
    for i in range(1,len(tim.snake_segments)):
        if tim.snake_segments[0].distance(tim.snake_segments[i]) < 18:
            score_board.game_over()
            game_is_on = False     
    
        
    
        
screen.exitonclick()
