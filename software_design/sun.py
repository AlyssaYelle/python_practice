
# File: Sun.py

# Description: Draws a sun like figure

import math, turtle

def drawArcR (ttl, size, degrees):
  for iter in range (degrees):
    ttl.forward (size)
    ttl.right (1)

def drawArcL (ttl, size, degrees):
  for iter in range (degrees):
    ttl.forward (size)
    ttl.left (1)

def drawRay (ttl, size):
  for iter in range (2):
    drawArcR (ttl, size, 90)
    drawArcL (ttl, size, 90)

def drawSun (ttl, size, color):
  ttl.fillcolor (color)
  ttl.begin_fill ()
  for iter in range (9):
    drawRay (ttl, size)
    ttl.right (160)
  ttl.end_fill ()

def main():
  # put label on top of page
  turtle.title ('Sun Figure')

  # setup screen size
  turtle.setup (1000, 1000, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # draw the sun figure
  drawSun (ttl, 1, 'red')

  # persist drawing
  turtle.done()

main()