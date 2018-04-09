# File: Squares.py

# Description: Draws squares of different sizes

import turtle

# draw a square of a given side 
# starting at uuper left corner (x, y)
def drawSquare (ttl, x, y, side):
  ttl.penup()
  ttl.goto(x, y)
  ttl.setheading(0)	# set the pen in the +ve x direction
  ttl.pendown()
  for iter in range (4):
    ttl.forward(side)
    ttl.right(90)
  ttl.penup()

def main():
  # put label on top of page
  turtle.title ('Squares')

  # setup screen size
  turtle.setup (800, 800, 0, 0)



  # create a turtle object
  ttl = turtle.Turtle()


  # assign a color to the turtle object
  ttl.color ('#841B2D')

  # assign shape turtle to the turtle object
  ttl.shape('turtle')


  # draw multiple squares
  drawSquare (ttl, -50, -50, 50)
  drawSquare (ttl, 0, 0, 50)
  drawSquare (ttl, 50, 50, 50)
  drawSquare (ttl, -50, 50, 150)

  # fill a closed region
  ttl.fillcolor ('#B284BE')
  ttl.begin_fill()
  drawSquare (ttl, 0, 0, 50)
  ttl.end_fill()


  # persist drawing
  turtle.done()

main()