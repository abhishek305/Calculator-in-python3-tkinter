import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Pentagon with Turtle")
screen.bgcolor("lightyellow")

# Create turtle
t = turtle.Turtle()
t.speed(5)
t.color("blue")
t.pensize(3)

# Draw a pentagon
sides = 5
length = 100  # length of each side
angle = 360 / sides  # turn angle

for _ in range(sides):
    t.forward(length)
    t.right(angle)

# Hide turtle
t.hideturtle()

# Keep window open
turtle.done()
