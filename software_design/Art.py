'''
This program uses the turtle graphics package to draw
a spooky ghost eyeball
whose eyebrows are on fleek
'''

import os
import turtle

# this function recursively draws a cool fanning pentagon design
# this design will represent the pupil of the eye
# the level of recursion dictates how dilated the pupil is
def draw_pentagons(ttl, start_x, start_y, line_length, recursion_level):
	ttl.color('black')
	ttl.penup()
	ttl.goto(start_x,start_y)
	ttl.pendown()
	if recursion_level > 0 and recursion_level <=6:
		ttl.forward(line_length)
		ttl.left(72)
		ttl.forward(line_length)
		ttl.left(72)
		ttl.forward(line_length)
		ttl.left(72)
		ttl.forward(line_length)
		ttl.left(72)
		ttl.forward(line_length)
		ttl.penup()
		line_length += 2
		recursion_level -=.1
		draw_pentagons(ttl, start_x, start_y, line_length,recursion_level)

# this function gives the eye winged liner sharp enough to cut a man
def draw_eyeliner(ttl):
	ttl.fillcolor('black')
	ttl.begin_fill()
	drawLine(ttl,-305,-55,-390,70)
	drawLine(ttl,-390,70,0,70)
	drawLine(ttl,0,70,-305,-55)
	ttl.end_fill()

# the title of this art is ghost so we want the background/skin to be a nice corpse grey
def fill_background(ttl,ul_x,ul_y,lr_x,lr_y):
	ttl.fillcolor('#B2BEB5')
	ttl.begin_fill()
	drawRectangle(ttl,ul_x,ul_y,lr_x,lr_y)
	ttl.end_fill()

# rectangles are useful
def drawRectangle(ttl, ul_x, ul_y, lr_x, lr_y):
	drawLine(ttl, ul_x, ul_y, ul_x, lr_y)
	drawLine(ttl, ul_x, lr_y, lr_x, lr_y)
	drawLine(ttl, lr_x, lr_y, lr_x, ul_y)
	drawLine(ttl, lr_x, ul_y, ul_x, ul_y)

# lines are REALLY useful
def drawLine (ttl, x1, y1, x2, y2):
	ttl.penup()
	ttl.goto(x1,y1)
	ttl.pendown()
	ttl.goto(x2,y2)
	ttl.penup()

# nice eye shape
def eye_outline(ttl):
	ttl.penup()
	ttl.goto(375,-100)
	ttl.fillcolor('#FEFEFA')
	ttl.begin_fill()
	ttl.pendown()
	ttl.left(115)
	ttl.circle(400,120)
	ttl.left(60)
	ttl.circle(400,120)
	ttl.end_fill()
	ttl.penup()

# this function recursively draws circles to fill in the iris of the eye
# it looks cooler than than just drawing a circle and filling it in
def iris(ttl, radius, bottom_x, bottom_y):
	ttl.color('#ACE5EE')
	if radius > 5:
		ttl.goto(bottom_x,bottom_y)

		ttl.pendown()
		ttl.circle(radius)
		ttl.penup()
		radius -= 5
		bottom_y += 5
		iris(ttl,radius, bottom_x,bottom_y)

# an eye needs an eyebrow
def eyebrow(ttl):
	ttl.color('#3B444B')
	ttl.fillcolor('#3B444B')
	ttl.begin_fill()
	drawLine(ttl,390,170,400,300)
	drawLine(ttl,400,300,0,350)
	drawLine(ttl,0,350,-400,250)
	drawLine(ttl,-400,250, 0,270)
	drawLine(ttl,0,270,390,170)
	ttl.end_fill()










def main():
	turtle.tracer(1000)

	recursion_level = int(input('Enter a level of recursion between 1 and 6: '))
	# give the art a title
	turtle.title('Ghost')

	# setup screen size
	turtle.setup(800,800,0)

	# create a turtle object
	ttl = turtle.Turtle()
	ttl.color('black')
	ttl.shape('turtle')


	# draw the picture
	fill_background(ttl,-400,400,400,-400)
	draw_eyeliner(ttl)
	eye_outline(ttl)
	ttl.right(45)
	iris(ttl, 198, 60,-265) 
	eyebrow(ttl)
	draw_pentagons(ttl, 45, -70, 4,recursion_level)


	# persist the drawing
	turtle.done()


main()







