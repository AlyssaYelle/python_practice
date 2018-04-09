# File: Hello.py

# Description: This program writes out Hello World

#do not ever have a variable named turtle when you're using turtle graphics
import turtle


def main():
  # put label on top of page
  turtle.title ('Hello World')

  # setup screen size
  turtle.setup (1000, 1000, 0, 0)
 
  # move turtle to origin
  turtle.penup()
  turtle.goto (0, 0)

  # set the color
  turtle.color ('#E52B50')
  turtle.shape('turtle')

  # write the message
  turtle.write ('i like your butt', font = ('Times New Roman', 36, 'bold'))

  # hide the turtle
  turtle.showturtle()

  # persist the drawing
  # without this line the drawing will vanish
  turtle.done()

main()