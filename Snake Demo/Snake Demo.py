#Snake Game
# by @TokyoEdTech

import os
import turtle
import time
import random
import math


delay = 0.1

#Score
score = 0
high_score = 0

#Setting up the screen
wn = turtle.Screen()
wn.title("Snake Demo")
wn.bgcolor("dark green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition (-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0   High Score: 0", align="center", font =("Courier", 20, "normal"))

#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance<18:
        return True
    else:
        return False

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")



#Main game loop
while True:
    wn.update()
    

    #Snake Food respawn
    #Check for collision with food
    if isCollision(head, food):
        #Reset the food
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.setposition(x, y)

        #Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("dark grey")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.00005
        
        #Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font =("Courier", 20, "normal"))

    #Move the end segment first in reverse
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    #Game Over Collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        #Clear the segments list
        segments.clear()

        #Reset the delay
        delay = 0.1

        #Reset the score
        score = 0

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font =("Courier", 20, "normal"))
        
    move()

    #Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            #Clear the segments list
            segments.clear()

            #Reset the score
            score = 0

            #Reset the delay
            delay = 0.1
            
            pen.clear()
            pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font =("Courier", 20, "normal"))

    time.sleep(delay)

wn.mainloop()
