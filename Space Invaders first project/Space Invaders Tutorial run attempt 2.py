#Space Invaders
#Set up the screen
#Create the Player Bullet and Fire with the Space Bar
#Python 3.8.6 on Windows
import turtle
import os
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("wp3284832.gif.gif")
wn.tracer(0)

#Register the shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
    
#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 0

#Choose a number of enemies
number_of_enemies = 30
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -230
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    #Update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0
        

enemyspeed = 0.2


#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("White")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.4, 0.5)
bullet.hideturtle()

bulletspeed = 0.2

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Move the player left and right
def move_left():
    global playerspeed
    playerspeed = -1.2
    
def move_right():
   global playerspeed
   playerspeed = 1.2

def stop_player():
    global playerspeed
    playerspeed =0

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition (x, y +10)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance<18:
        return True
    else:
        return False

#Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")
wn.onkeyrelease(stop_player, "Left")
wn.onkeyrelease(stop_player, "Right")

#Main game loop
while True:
    wn.update()

    #Move the player
    player.setx(player.xcor()+ playerspeed)

    #Check borders
    if player.xcor() > 285:
        player.setx(285)
        playerspeed =0

    elif player.xcor() < -285:
        player.setx(-285)
        playerspeed =0
    
    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        #Move the enemy back and down
        if enemy.xcor() > 285:
            #Move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1
            
        if enemy.xcor() < -285:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        #Check for collision between bullet and enemy
        if isCollision(bullet, enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-230, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            
            
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break

        #Move the bullet
        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        #Check to see if the bullet has gone to top
        if bullet.ycor() > 280:
            bullet.hideturtle()
            bulletstate = "ready"
        

