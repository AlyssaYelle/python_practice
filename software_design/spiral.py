
import turtle

# draw spiral recursively
def drawSpiral (ttl, step, decay, angle):
  if step > 0:
    ttl.forward (step)
    ttl.left (angle)
    step = step - decay
    drawSpiral (ttl, step, decay, angle)

def main():
  # prompt the user to enter a step size
  step = int (input ('Enter step size: '))

  # prompt the user to enter a decay rate
  decay = int (input ('Enter a decay rate: '))

  # prompt the user to enter an angle
  angle = int (input ('Enter an angle to turn: '))

  # put label on top of page
  turtle.title ('Spira Mirabilis')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create Turtle object
  ttl = turtle.Turtle()

  # assign a color to the turtle object
  ttl.color ('navy')

  # draw the spiral
  ttl.penup()
  ttl.goto (-200, -200)
  ttl.pendown()
  drawSpiral (ttl, step, decay, angle)
  ttl.penup()

  # persist drawing
  turtle.done()


main()