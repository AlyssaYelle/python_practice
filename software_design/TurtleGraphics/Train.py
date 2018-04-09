'''
PYTHON 3
a cute turtle named Clarence introduces himself
and then draws a pretty choo choo train
using turtle graphics
'''

import turtle

# draw a line from (x1,y1) to (x2,y2)
def drawLine (ttl, x1, y1, x2, y2):
	ttl.penup()
	ttl.goto(x1,y1)
	ttl.pendown()
	ttl.goto(x2,y2)
	ttl.penup()

def drawRectangle(ttl, ul_x, ul_y, lr_x, lr_y):
	drawLine(ttl, ul_x, ul_y, ul_x, lr_y)
	drawLine(ttl, ul_x, lr_y, lr_x, lr_y)
	drawLine(ttl, lr_x, lr_y, lr_x, ul_y)
	drawLine(ttl, lr_x, ul_y, ul_x, ul_y)

def train_accessories(ttl):
	# smokestack
	drawLine(ttl,260,200,240,330)
	drawLine(ttl,240,330,260,350)
	drawLine(ttl,260,350,300,350)
	drawLine(ttl,300,350,320,330)
	drawLine(ttl,320,330,300,200)
	drawLine(ttl,240,330,320,330)

	# top stacked rectangles
	ttl.fillcolor('#330066')
	ttl.begin_fill()
	drawRectangle(ttl,50,220,150,200)
	ttl.end_fill()
	ttl.fillcolor('#9955BB')
	ttl.begin_fill()
	drawRectangle(ttl,75,240,125,220)
	ttl.end_fill()

	# front stacked rectangles
	ttl.fillcolor('#330066')
	ttl.begin_fill()
	drawRectangle(ttl,340,180,350,0)
	ttl.end_fill()
	ttl.fillcolor('#9955BB')
	ttl.begin_fill()
	drawRectangle(ttl,350,140,360,40)
	ttl.end_fill()

	# nose
	drawLine(ttl, 340,-100,340,-250)
	drawLine(ttl, 340,-250,390,-250)
	drawLine(ttl,390,-250,350,-100)
	drawLine(ttl,350,-100,340,-100)
	
	
def train_windows(ttl):
	ttl.fillcolor('#630F0F')
	ttl.begin_fill()
	drawRectangle(ttl,-330,270,-240,100)
	ttl.end_fill()
	ttl.fillcolor('#630F0F')
	ttl.begin_fill()
	drawRectangle(ttl,-210,270,-120,100)
	ttl.end_fill()


def decorative_stripes(ttl):
	# stripes
	ttl.color('#EFBBCC')
	ttl.fillcolor('#EFBBCC')
	ttl.begin_fill()
	drawRectangle(ttl,-100,40,340,0)
	ttl.end_fill()
	ttl.fillcolor('#EFBBCC')
	ttl.begin_fill()
	drawRectangle(ttl,-40,200,-10,40)
	ttl.end_fill()
	ttl.fillcolor('#EFBBCC')
	ttl.begin_fill()
	drawRectangle(ttl,190,200,220,40)
	ttl.end_fill()

	# polka dots
	x = -95
	y = 15
	while (x <340):
		ttl.penup()
		ttl.goto(x,y)
		ttl.pendown()
		ttl.fillcolor('#841B2D')
		ttl.begin_fill()
		ttl.circle(5)
		ttl.end_fill()
		x += 15

	x = -25
	y = 195
	while (y >40):
		ttl.penup()
		ttl.goto(x,y)
		ttl.pendown()
		ttl.fillcolor('#841B2D')
		ttl.begin_fill()
		ttl.circle(5)
		ttl.end_fill()
		y -= 15

	x = 205
	y = 195
	while (y >40):
		ttl.penup()
		ttl.goto(x,y)
		ttl.pendown()
		ttl.fillcolor('#841B2D')
		ttl.begin_fill()
		ttl.circle(5)
		ttl.end_fill()
		y -= 15

def train_outline(ttl):
	#back section of train
	drawLine(ttl, -320,-200,-350,-200)
	drawLine(ttl, -350,-200,-350,300)
	ttl.fillcolor('#CD607E')
	ttl.begin_fill()
	drawRectangle(ttl, -370,330,-80,300)
	ttl.end_fill()
	drawLine(ttl, -100,300,-100,-200)

	#bottom of train (no wheel arches yet)
	ttl.penup()
	ttl.goto(-140,-200)
	ttl.pendown()
	ttl.left(90)
	ttl.circle(90,180)
	drawLine(ttl, -140,-200,-60,-200)
	ttl.goto(120,-200)
	ttl.left(180)
	ttl.pendown()
	ttl.circle(90,180)
	drawLine(ttl, 120,-200,140,-200)
	ttl.goto(320,-200)
	ttl.left(180)
	ttl.pendown()
	ttl.circle(90,180)
	drawLine(ttl,320,-200,340,-200)

	#draw front of train
	drawLine(ttl, 340,-200,340,200)
	drawLine(ttl, 340,200,-100,200)

def draw_wheels(ttl, x, y, larger_r, smaller_r):
	inc = turtle.Turtle()
	inc.speed(0)
	inc.penup()
	inc.goto(x, y + larger_r - smaller_r)

	inc.color('#843F5B')
	inc.shape('turtle')
	ttl.color('#734F96')
	
	ttl.penup()
	ttl.setheading(0)
	
	ttl.goto(x, y)
	ttl.pendown()
	ttl.circle(larger_r)
	ttl.penup()

	spoke_angle = 5
	for r in range(2):
		for q in range(9):
			inc.goto(x, y + larger_r - smaller_r)
			inc.pendown()
			inc.circle(smaller_r, q * 45)
			ttl.goto(x, y + smaller_r)
			ttl.pendown()
			ttl.circle(larger_r - smaller_r, spoke_angle)
			ttl.goto(inc.position())
			inc.penup()
			ttl.penup()
			spoke_angle += 45
			inc.setheading(0)
			ttl.setheading(0)
		spoke_angle = -5

	inc.ht()
	ttl.ht()



def train_tracks(ttl):
	# main tracks
	ttl.fillcolor('#841B2D')
	ttl.begin_fill()
	drawRectangle(ttl,-400,-290,400,-300)
	ttl.end_fill()
	
	ul_x = -380
	ul_y = -300
	lr_x = -350
	lr_y = -310
	while (lr_x <400):
		ttl.fillcolor('#841B2D')
		ttl.begin_fill()
		drawRectangle(ttl,ul_x,ul_y,lr_x,lr_y)
		ttl.end_fill()
		ul_x += 60
		lr_x += 60


def main():

	# Label the drawing
	turtle.title('Here is a pretty choo-choo train drawn by a cute turtle named Clarence.')

	# setup screen size
	turtle.setup(800,800,0)

	# create a turtle object
	ttl = turtle.Turtle()


	# set the color to Deep Green
	ttl.color('#056608')

	# set turtle to turtle
	ttl.shape('turtle')

	# Clarence introduces himself
	# move turtle to (-330,80)
	ttl.penup()
	ttl.goto(-280,30)
	ttl.write ('Hello! \nMy name is Clarence \nand I am going to draw \na cute choo-choo train', font = ('Times New Roman', 12, 'bold'))
	
	# set the color to Antique Ruby
	ttl.color('#841B2D')

	# draw the train tracks
	train_tracks(ttl)

	# draw the train outline
	train_outline(ttl)

	# draw the train's accessories
	train_accessories(ttl)

	# draw the train windows
	train_windows(ttl)

	# draw the decorative strips
	decorative_stripes(ttl)
	
	# draw wheels
	
	draw_wheels(ttl, -230, -290, 80,70)
	draw_wheels(ttl, 30, -290, 80,70)
	draw_wheels(ttl, 230, -290, 80,70)
	

	
	# persist the drawing
	turtle.done()


main()



















