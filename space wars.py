# Turtle graphics

import turtle
import math
import random
import playsound

# set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.bgpic("Colorful-Stars.gif")
wn.tracer(3)

# Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
playsound.playsound("game.mp3")

# Create a player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()              # Does not leave a line trail, by default it does
#player.speed(0)            # Animation speed

# Create a score variable
score = 0

# Create multiple enemies
maxgoals = 9
enemies = []

for count in range(maxgoals):
    # Create enemies
    enemies.append(turtle.Turtle())
    enemies[count].color("red")
    enemies[count].shape("circle")
    enemies[count].penup()
    enemies[count].speed(0)
    enemies[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

# Set speed variable
speed = 1

# Define functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    if speed > 0:
        speed -= 1

def iscollision(t1, t2):
    # Pythagoras Theorem to get the hypotenuse = SqRoot(square(x dist) + square(y dist))
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

# Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)


    # Boundary Checking for player
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)

    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)

    # Enemy speed and enemy movement
    for count in range(maxgoals):
        enemies[count].forward(2)

        # Boundary Checking for enemies
        if enemies[count].xcor() > 290 or enemies[count].xcor() < -290:
            enemies[count].right(180)

        if enemies[count].ycor() > 290 or enemies[count].ycor() < -290:
            enemies[count].right(180)

        # Collision Checking
        if iscollision(player, enemies[count]):
            enemies[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            enemies[count].right(random.randint(0, 360))
            score += 1
            # Draw score on screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" % score
            mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


delay = raw_input("Press enter to finish")