from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
import random
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
game_ball = Ball()



screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_down,"s")

game_on=True
while game_on:
  time.sleep(0.1)
  screen.update()
  game_ball.move()
  if game_ball.ycor() > 280 or game_ball.ycor() < -280:
    game_ball.bounce_y()

  if game_ball.distance(r_paddle) < 50 and game_ball.xcor() >320:
    game_ball.bounce_x()

  if game_ball.distance(l_paddle) <50 and game_ball.xcor() <-320:
    game_ball.bounce_x()

  if game_ball.xcor() > 380:
    game_on = False
    game_over = Turtle()
    game_over.color("white") 
    game_over.write("GAME OVER!, LEFT PLAYER WINS!",align="center",font=("Courier",26,"normal"))
  if game_ball.xcor() <  -380:
    game_on = False
    game_over = Turtle()
    game_over.color("white") 
    game_over.write("GAME OVER!, RIGHT PLAYER WINS!",align="center",font=("Courier",26,"normal"))


screen.exitonclick()