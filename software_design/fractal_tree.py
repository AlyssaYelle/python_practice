
import turtle

# draw a tree recursively
def drawTree (ttl, length):
  if length > 5:
    ttl.forward (length)
    ttl.right (20)
    drawTree (ttl, length - 15)
    ttl.left (40)
    drawTree (ttl, length - 15)
    ttl.right (20)
    ttl.backward (length)

def main():
  # prompt the user to enter a branch length
  length = int (input ('Enter branch length: '))

  # put label on top of page
  turtle.title ('Recursive Tree')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create Turtle object
  ttl = turtle.Turtle()

  # assign a color to the turtle object
  ttl.color ('green')

  # draw the tree
  ttl.penup()
  ttl.goto (0, -100)
  ttl.pendown()
  ttl.left (90)
  ttl.pendown()
  drawTree (ttl, length)
  ttl.penup()

  # persist drawing
  turtle.done()


main()