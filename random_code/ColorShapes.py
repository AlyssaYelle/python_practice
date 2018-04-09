# File: ColorShapes.py

# Description: Draws filled in shapes

import turtle

def main():
  # put label on top of page
  turtle.title ('Colorful Shapes')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # draw a triangle
  turtle.pensize(3)
  turtle.penup()
  turtle.goto (-200, -50)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color ('red')
  turtle.circle (40, steps = 3)
  turtle.end_fill()

  # draw a square
  turtle.penup()
  turtle.goto (-100, -50)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color ('navy')
  turtle.circle (40, steps = 4)
  turtle.end_fill()

  # draw a pentagon
  turtle.penup()
  turtle.goto (0, -50)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color ('green')
  turtle.circle (40, steps = 5)
  turtle.end_fill()

  # draw a hexagon
  turtle.penup()
  turtle.goto (100, -50)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color ('yellow')
  turtle.circle (40, steps = 6)
  turtle.end_fill()

  # draw a circle
  turtle.penup()
  turtle.goto (200, -50)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color ('purple')
  turtle.circle (40)
  turtle.end_fill()

  # write header
  turtle.penup()
  turtle.goto (-100, 50)
  turtle.write ('Cool Colorful Shapes', font = ('Times', 18, 'bold'))

  # hide turtle
  turtle.hideturtle()

  # persist drawing
  turtle.done()

main()
