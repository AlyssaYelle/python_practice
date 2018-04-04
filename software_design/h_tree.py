
import turtle

# draw a line from point p1 to point p2
def drawLine (ttl, p1, p2):
  x1 = p1[0]
  y1 = p1[1]
  x2 = p2[0]
  y2 = p2[1]
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# draw h tree recursively
def draw_htree (ttl, order, p, side):

  if (order > 0):
    # define the end points of the H
    p1 = [p[0] - side // 2, p[1] + side // 2]
    p2 = [p[0] - side // 2, p[1] - side // 2]
    p3 = [p[0] + side // 2, p[1] + side // 2]
    p4 = [p[0] + side // 2, p[1] - side // 2]

    # draw the H shape
    drawLine (ttl, [p[0] - side // 2, p[1]], [p[0] + side // 2, p[1]])
    drawLine (ttl, p1, p2)
    drawLine (ttl, p3, p4)

    # recursively draw the H shapes at the end points
    draw_htree (ttl, order - 1, p1, side // 2)
    draw_htree (ttl, order - 1, p2, side // 2)
    draw_htree (ttl, order - 1, p3, side // 2)
    draw_htree (ttl, order - 1, p4, side // 2)

def main():
  # prompt the user to enter an order for the H Tree
  order = int (input ('Enter an order: '))

  # prompt the user to enter the length of a side
  side = int (input ('Enter side: '))

  # put label on top of page
  turtle.title ('H Tree')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # assign a color to the turtle object
  ttl.color ('navy')

  # draw the H Tree
  p = [0, 0]
  draw_htree (ttl, order, p, side)

  # persist drawing
  turtle.done()


main()