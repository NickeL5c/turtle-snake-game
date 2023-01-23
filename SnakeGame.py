# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:28:31 2023

@author: E40022130
"""

# import turtle graphics module
import turtle
import random

# define unchanging variables
WIDTH = 1480  # width of game in pixels
HEIGHT = 800  # height of game in pixels
DELAY = 100  # milliseconds between screen updates
FOOD_SIZE = 20  # pixels


firstTime = True  # so we know if it is first time or not

# set dictionary of directions for snake
offsets = {
    "u": (0, 20),
    "d": (0, -20),
    "l": (-20, 0),
    "r": (20, 0),
        }


# set snake direction if keys pressed
def bindDirKeys():
    screen.onkey(lambda: setSnakeDir("u",1), "Up")
    screen.onkey(lambda: setSnakeDir("l",1), "Left")
    screen.onkey(lambda: setSnakeDir("d",1), "Down")
    screen.onkey(lambda: setSnakeDir("r",1), "Right")
    screen.onkey(lambda: setSnakeDir("u",2), "w")
    screen.onkey(lambda: setSnakeDir("l",2), "a")
    screen.onkey(lambda: setSnakeDir("d",2), "s")
    screen.onkey(lambda: setSnakeDir("r",2), "d")
    screen.onkey(lambda: turtle.done(), "Escape")


# set snake directions on key strokes calling setSnakeDir
def setSnakeDir(dir, player):
    global snake1Dir, snake2Dir
    if player == 1:
        if dir == "d":
            if snake1Dir != "u": # checks if snake tries to run into itself backwards
                snake1Dir = "d"
        if dir == "u":
            if snake1Dir != "d":
                snake1Dir = "u"
        if dir == "r":
            if snake1Dir != "l":
                snake1Dir = "r"
        if dir == "l":
            if snake1Dir != "r":
                snake1Dir = "l"

    if player == 2:
        if dir == "d":
            if snake2Dir != "u": # checks if snake tries to run into itself backwards
                snake2Dir = "d"
        if dir == "u":
            if snake2Dir != "d":
                snake2Dir = "u"
        if dir == "r":
            if snake2Dir != "l":
                snake2Dir = "r"
        if dir == "l":
            if snake2Dir != "r":
                snake2Dir = "l"


def clearTurtles():
    stamper1.clear()
    stamper1.hideturtle()
    start.clear()
    start.hideturtle()
    food.clear()
    food.hideturtle()
    stamper2.clear()
    stamper2.hideturtle()


def clearStamps():
    stamper1.clear()
    stamper2.clear()
    start.clear()
    food.clear()

def collision(player, newHead):
    global snake1, snake2, highScore

    if player == 1:
        if newHead in snake1 or newHead in snake2 or newHead[0] < -WIDTH/2 or newHead[0] > WIDTH/2 \
            or newHead[1] < -HEIGHT/2 or newHead[1] > HEIGHT/2:
            if score1 > highScore:
                highScore = score1
            return True
    if player == 2:
        if newHead in snake2 or newHead in snake1 or newHead[0] < -WIDTH / 2 or newHead[0] > WIDTH/2 \
            or newHead[1] < -HEIGHT / 2 or newHead[1] > HEIGHT / 2:
            if score2 > highScore:
                highScore = score2
            return True


def startWindow():
    global highScore, firstTime

    clearTurtles()
    screen.update()

    start.goto(0, 100)

    if firstTime:
        highScore = 0
        firstTime = False
    else:
        if score1 > score2:
            start.write("Player 1 is the winner!", align="center", font=("Times New Roman", 40, "normal"))
        if score2 > score1:
            start.write("Player 2 is the winner!", align="center", font=("Times New Roman", 40, "normal"))
        if score1 == score2:
            start.write("It was a tie!", align="center", font=("Times New Roman", 40, "normal"))

    start.goto(0, -150)
    start.write(f"Welcome to the Snake Game!\nAre there 1 or 2 numPlayers?\n"
                f"(click '1' for 1P or '2' for 2P)\nHigh Score: {highScore}",
                align="center", font=("Times New Roman", 40, "normal"))

    
    
    screen.onkey(reset1(), "1")
    screen.onkey(reset2(), "2")
    screen.listen()

    # if player choose 1, then execute reset function

def reset1():
    global score1, score2, snake1, snake2, snake1Dir, foodPos, gameOver1, gameOver2
    # set both numPlayers to not game over

    gameOver1 = False
    gameOver2 = True

    # make list of lists to store snake body part positions
    snake1 = [[0, 0], [20, 0], [40, 0], [60, 0], [80, 0], [100, 0]]
    snake2 = [1,2,3,4,5]
    # draw snakefirst time

    for segment in snake1:
        stamper1.goto(segment[0], segment[1])
        stamper1.stamp()
    
    #make snake blink a few times before start
    #if numPlayers == 1:
     #   for i in range(5):
      #      turtle.ontimer(stamper1.stamp, 1000)


        #for i in range(5):
         #   turtle.ontimer(stamper1.stamp, 1000)
          #  turtle.ontimer(stamper2.stamp, 1000)

    # initial direction set for snake
    snake1Dir = "u"

    # initial score
    score1 = 0
    score2 = 0
    
    # initial position of food
    foodPos = getRandomFoodPos()
    food.goto(foodPos)
    gameLoop()

def reset2():
    global score1, score2, snake1, snake2, snake1Dir, snake2Dir, foodPos, gameOver1, gameOver2
    # set both numPlayers to not game over

    gameOver1 = False
    gameOver2 = False

    # make list of lists to store snake body part positions
    snake1 = [[0, 0], [20, 0], [40, 0], [60, 0], [80, 0], [100, 0]]

    snake2 = [[0, 0], [-20, 0], [-40, 0], [-60, 0], [-80, 0], [-100, 0]]
    # draw snakefirst time

    for segment in snake1:
        stamper1.goto(segment[0], segment[1])
        stamper1.stamp()

    for segment in snake2:
            stamper2.goto(segment[0], segment[1])
            stamper2.stamp()
    
    #make snake blink a few times before start
    #if numPlayers == 1:
     #   for i in range(5):
      #      turtle.ontimer(stamper1.stamp, 1000)


        #for i in range(5):
         #   turtle.ontimer(stamper1.stamp, 1000)
          #  turtle.ontimer(stamper2.stamp, 1000)

    # initial direction set for snake
    snake1Dir = "u"
    snake2Dir = "d"

    # initial score
    score1 = 0
    score2 = 0
    
    # initial position of food
    foodPos = getRandomFoodPos()
    food.goto(foodPos)
    gameLoop()


# starts game loop
def gameLoop():
    global highScore, gameOver1, gameOver2, snake1Dir, snake2Dir
    clearStamps() # Removes all stamps currently on screen
    screen.update()
    
    # make a new head for snake 1 in correct direction
    if not gameOver1:
        newHead1 = snake1[-1].copy()
        newHead1[0] += offsets[snake1Dir][0]
        newHead1[1] += offsets[snake1Dir][1]

        # check collisions with self, other snake or wall
        if collision(1, newHead1):
            gameOver1 = True

    # make a new head for snake 2 in correct direction
    if not gameOver2:
        newHead2 = snake2[-1].copy()
        newHead2[0] += offsets[snake2Dir][0]
        newHead2[1] += offsets[snake2Dir][1]

        if collision(2, newHead2):
            gameOver2 == True
    

    if gameOver1 and gameOver2:
        startWindow()
    else:
        # put new head on snake body
        if not gameOver1:
            snake1.append(newHead1)

             # check for food collision
            if not foodCollision(1):
                snake1.pop(0) # keep snake same length unless eat food

            for segment in snake1:
                stamper1.goto(segment[0], segment[1])
                stamper1.stamp()





        if not gameOver2:
            snake2.append(newHead2)
        
            if not foodCollision(2):
                snake2.pop(0)  # keep snake same length unless eat food

        # draw the new snake
            for segment in snake2:
                stamper2.goto(segment[0], segment[1])
                stamper2.stamp()
            
        # refresh the screen with new score
        screen.title(f"SNAKE GAME! P1 Score: {score1}, P2 Score: {score2}")
        food.stamp()
        screen.update()
        
        # do it a lot
        turtle.ontimer(gameLoop, DELAY)


# checks for collision with snake food
def foodCollision(player):
    global foodPos, score1, score2
    if player == 1:
        if snake1[-1] == foodPos:
            foodPos = getRandomFoodPos()  # assign new food position
            food.goto(foodPos)  # put food at new position
            score1 += 1
            return True
    if player == 2:
        if snake2[-1] == foodPos:
            foodPos = getRandomFoodPos()  # assign new food position
            food.goto(foodPos)  # put food at new position
            score2 += 1
            return True
    return False


# gets new random food position
def getRandomFoodPos():
    # setting random position anywhere between edges with food size in mind
    # but also using increments of 20 so collisions can occur
    x = 20*random.randint((-WIDTH/2 + 2*FOOD_SIZE)/20, (WIDTH/2 - 2*FOOD_SIZE)/20)
    y = 20*random.randint((-HEIGHT/2 + 2*FOOD_SIZE)/20, (HEIGHT/2 - 2*FOOD_SIZE)/20)
    return [x, y]


# make a controllable window object for game
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # set dimensions of window
screen.screensize(WIDTH, HEIGHT)
screen.title("SNAKE GAME!")
screen.bgcolor("black")
screen.tracer(0)  # turns off auto animation mostly

# create stamper object for snake body parts
stamper1 = turtle.Turtle()
stamper1.shape("circle")
stamper1.color("red")
stamper1.shapesize(25/20)
stamper1.penup()  # lifts up stamper when moving

stamper2 = turtle.Turtle()
stamper2.shape("circle")
stamper2.color("blue")
stamper2.shapesize(25/20)
stamper2.penup()

food = turtle.Turtle()
food.shape("turtle")
food.color("green")
food.shapesize(FOOD_SIZE/20)
food.penup()

start = turtle.Turtle()
start.color("white")
start.penup()

# event handlers
bindDirKeys()
screen.listen()
    
# start game
startWindow()


# needed to end turtle programs
turtle.done()
