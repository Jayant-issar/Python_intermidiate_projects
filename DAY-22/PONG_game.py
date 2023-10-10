import time
from turtle import Turtle, Screen


#making the screen        
screen = Screen()
screen.screensize(600,500)
screen.bgcolor("cyan")
screen.title("Pong game")
screen.listen()
screen.tracer(0)
game_running = True


# creating the paddle class
class Paddle(Turtle):
    def __init__(self, position_x, positon_y, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        
        self.seth(90)
        self.shape("square")
        self.shapesize(1,4.5)
        self.color("black")
        self.penup()
        self.goto(position_x, positon_y)
        
    # methods for moving up and down
    def up(self):
        if self.ycor() < 240:
            self.forward(30)
    def down(self):
        if self.ycor() > -240:
            self.forward(-30)


paddle_1 = Paddle(315,0)
paddle_2 = Paddle(-320,0)


#binding keys to paddles
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")


# creating the ball class
class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("red")
        self.penup()
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.12
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def y_bounce(self):
        self.y_move *= -1       
    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.95
    
    def restart(self):
        self.goto(0,0)    

class ScoreBoard(Turtle):
    def __init__(self,x,y, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.write(f"{self.score}",align="center",font=("Arial", 50, "normal") )
        
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}",align="center",font=("Arial", 50, "normal") )
    
    
r_score_board = ScoreBoard(85,220)
l_score_board = ScoreBoard(-85,220)



ball = Ball()


while game_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #bouncing from vertical walls
    if ball.ycor()>= 278 or ball.ycor() <= -278:
        ball.y_bounce()
    
    # decting game over
    if ball.xcor() > 320:
        l_score_board.increase_score()
        ball.restart()
        
    elif ball.xcor() < -320:
        r_score_board.increase_score()
        ball.restart()
        
    # checking the collison with paddle
    if ball.distance(paddle_1) <= 49.25 and ball.xcor() > 290:
        ball.x_bounce()
    
    if ball.distance(paddle_2) <= 49.25 and ball.xcor() < -290:
        ball.x_bounce()
    
    
            



screen.exitonclick()