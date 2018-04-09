# File: RandomWalk.py

# Description: Draws a grid and exhibits a random walk

import turtle, random

def main():
  # put label on top of page
  turtle.title ('Random Walk')

  # setup screen size
  turtle.setup (1000, 1000, 0, 0)

  # set turtle speed
  #turtle.speed (1)

  # draw 16 x 16 lattice
  turtle.color ('gray')
  
  # draw horizontal lines
  x = -80
  for y in range (-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto (x, y)
    turtle.pendown()
    turtle.forward (160)

  # draw vertical lines
  y = 80
  turtle.right (90)
  for x in range (-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto (x, y)
    turtle.pendown()
    turtle.forward (160)

  # start random walk
  turtle.pensize(3)
  turtle.color ('red')
 
  turtle.penup()
  turtle.goto(0, 0)
  turtle.pendown()

  x = y = 0
  while (abs(x) < 80 and abs(y) < 80):
    r = random.randint(0, 3)
    if r == 0:
      x += 10
      turtle.setheading(0)
      turtle.forward(10)    
    elif r == 1:
      y -= 10
      turtle.setheading(270)
      turtle.forward(10)    
    elif r == 2:
      x -= 10
      turtle.setheading(180)
      turtle.forward(10)    
    elif r == 3:
      y += 10
      turtle.setheading(90)
      turtle.forward(10)    

  # persist drawing
  turtle.done()

main()


# File: Sierpinski.py

# Description: Draws Sierpinski's Curve or Gasket

import math, turtle

def drawGasket (ttl, size):
  if size < 10:
    return
  for iter in range (3):
    ttl.forward (size / 2)
    insertGasket (ttl, size)
    ttl.forward (size / 2)
    ttl.right (120)

def insertGasket (ttl, size):
  ttl.left (120)
  drawGasket (ttl, size / 2)
  ttl.right (120)

def oneSide (ttl, s, diag, level):
  if (level == 0):
    return
  else:
    oneSide (ttl, s, diag, level - 1)
    ttl.right (45); ttl.forward (diag); ttl.right (45)
    oneSide (ttl, s, diag, level - 1)
    ttl.left (90); ttl.forward (s); ttl.left (90)
    oneSide (ttl, s, diag, level - 1)
    ttl.right (45); ttl.forward (diag); ttl.right (45)
    oneSide (ttl, s, diag, level - 1)

def curve (ttl, s, level):
  diag = s / math.sqrt (2)
  for iter in range (4):
    oneSide (ttl, s, diag, level)
    ttl.right (45)
    ttl.forward (diag)
    ttl.right (45)

def main():
  # put label on top of page
  turtle.title ('Recursive Figures')

  # setup screen size
  turtle.setup (1000, 1000, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # draw the sierpinski curve
  # curve (ttl, 15, 3)

  # draw gasket
  drawGasket (ttl, 200)

  # persist drawing
  turtle.done()

main()
