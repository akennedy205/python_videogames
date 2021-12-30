#Space War tutorial @TokyoEdTech
#Part I: getting started

import os
import math
import random

#Import the turtle module
import turtle
turtle.fd(0)
#Set theanimation speed to the maximum
turtle.speed(0)
#Change background color
turtle.bgcolor("black")
#Hide default turtle
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

#Create my sprites
player = Sprite("triangle", "white", 0, 0)
player.setheading(90)

#Main game loop









