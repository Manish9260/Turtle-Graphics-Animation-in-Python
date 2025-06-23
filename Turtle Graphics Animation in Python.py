#Follow Me Id Coding With Manish And TechManish Youtube channel..
from turtle import *
from colorsys import hsv_to_rgb

# Setup
colormode(1)  # RGB values will be in the range [0, 1]
setpos(0, 80)
speed(0)
bgcolor('black')
pensize(2)

h = 0.71

# Drawing loop
for i in range(150):
    c = hsv_to_rgb(h, 1, 1)  # Get RGB tuple in 0-1 range
    color(c)  # Set turtle color
    h += 0.004

    circle(139, 90)
    left(90)
    left(20)
    circle(130, 90)
    left(18)

# Final message
penup()
goto(-250, -200)
color('white')
write("Welcome to YouTube Channel TechManish 👍👍", font=("Arial", 18, "bold"))
hideturtle()
done()
