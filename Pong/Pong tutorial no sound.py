#Simple Pong in Python 3 for Beginners

import turtle
import os
import winsound


wn = turtle.Screen()
wn.title("Pong test-run")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer (0)

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition (-400, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(1):
    border_pen.fd(800)
    border_pen.lt(90)
    border_pen.fd(600)
    border_pen.lt(90)
    border_pen.fd(800)
    border_pen.lt(90)
    border_pen.fd(600)
border_pen.hideturtle()

#Score
score_a = 0
score_b =0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.7
ball.dy = 0.65


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font =("Courier", 20, "normal"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down,"Down")

    
#Main Game loop
while True:
    wn.update()

    #Border checking the paddles
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    elif paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    elif paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking the ball
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font =("Courier", 20, "normal"))
        
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font =("Courier", 20, "normal"))
        
       
    #Paddle and ball collisions
    if (ball.xcor()> 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        



        
