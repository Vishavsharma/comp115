import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Mandala")

# Create a turtle
mandala = turtle.Turtle()
mandala.speed(0)  # Set the speed to the fastest

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        mandala.forward(side_length)
        mandala.right(90)

# Function to draw a mandala
def draw_mandala(num_squares, side_length):
    angle = 360 / num_squares
    for _ in range(num_squares):
        draw_square(side_length)
        mandala.right(angle)

# Draw the mandala
draw_mandala(36, 100)  # You can adjust the number of squares and their size as needed

# Hide the turtle
mandala.hideturtle()

# Keep the window open
turtle.done()
