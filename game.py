import turtle
import time
import random

delay = 0.1

# Score
# This will be the default score board of the game
score = 0
high_score = 0

# Set up the screen
# I set up the screen of the game and set up the color, size, and title
gamewindow = turtle.Screen()
gamewindow.title("The Snake Game, use WASD keys to move")
gamewindow.bgcolor("blue")
gamewindow.setup(width=600, height=600)
gamewindow.tracer(0)  # Turns off the screen updates

# Snake head
# This is where I set up my snake head in terms of size, shape, and color
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
# This is where I set up my snake food in terms of colour, size, and shape
sfood = turtle.Turtle()
sfood.speed(0)
sfood.shape("circle")
sfood.color("red")
sfood.penup()
sfood.goto(0, 100)

segments = []

# Pen
# I used pen to create the score board for the game and picked a font and size
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
# These are the main functions of the game so the snake can move in every direction
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings

# I used the WASD keys as the bindings and set each letter up with a direction
gamewindow.listen()
gamewindow.onkeypress(go_up, "w")
gamewindow.onkeypress(go_down, "s")
gamewindow.onkeypress(go_left, "a")
gamewindow.onkeypress(go_right, "d")

# Main game loop
# I used a while loop for the main game loop, if the loop is "true" the game will run
while True:
    gamewindow.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for a collision with the food
    if head.distance(sfood) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        sfood.goto(x, y)

        # Add a segment
        # this is the snake head's body and it will be a grey colour and have a square shape
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
