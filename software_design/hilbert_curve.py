
import turtle

def upperU (ttl, order, length):
  if order > 0:
    leftU (ttl, order - 1, length)
    ttl.setheading (270)
    ttl.forward (length) 
    upperU (ttl, order - 1, length)
    ttl.setheading (0)
    ttl.forward (length)
    upperU (ttl, order - 1, length)
    ttl.setheading (90)
    ttl.forward (length)
    rightU (ttl, order - 1, length)

def leftU (ttl, order, length):
  if order > 0:
    upperU (ttl, order - 1, length)
    ttl.setheading (0)
    ttl.forward (length) 
    leftU (ttl, order - 1, length)
    ttl.setheading (270)
    ttl.forward (length)
    leftU (ttl, order - 1, length)
    ttl.setheading (180)
    ttl.forward (length)
    downU (ttl, order - 1, length)

def rightU (ttl, order, length):
  if order > 0:
    downU (ttl, order - 1, length)
    ttl.setheading (180)
    ttl.forward (length) 
    rightU (ttl, order - 1, length)
    ttl.setheading (90)
    ttl.forward (length)
    rightU (ttl, order - 1, length)
    ttl.setheading (0)
    ttl.forward (length)
    upperU (ttl, order - 1, length)

def downU (ttl, order, length):
  if order > 0:
    rightU (ttl, order - 1, length)
    ttl.setheading (90)
    ttl.forward (length) 
    downU (ttl, order - 1, length)
    ttl.setheading (180)
    ttl.forward (length)
    downU (ttl, order - 1, length)
    ttl.setheading (270)
    ttl.forward (length)
    leftU (ttl, order - 1, length)

def draw_hilbert (ttl, order, size, length):
  for iter in range (order):
    length = length // 2

  # get the starting point
  x = (-1) * size // 2 + length // 2
  y = size // 2 - length // 2

  # start drawing
  ttl.penup ()
  ttl.goto (x, y)
  ttl.pendown ()
  upperU (ttl, order, length)

def main():
  # prompt the user to enter an order for the Hilbert Curve
  order = int (input ('Enter an order: '))

  # put label on top of page
  turtle.title ('Hilbert Curve')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # assign a color to the turtle object
  ttl.color ('navy')

  # draw the hilbert curve
  size = 200
  length = 200
  draw_hilbert (ttl, order, size, length)

  # persist drawing
  turtle.done()


main()