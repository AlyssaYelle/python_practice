'''
The purpose of this program is to create simple geometric objects
(point, circle, rectangle)
and write helpful methods for them.
We then test these methods in main
'''


import math

class Point (object):
  # constructor 
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  def does_intersect (self, c):
    return self.center.dist(c.center) < (c.radius + self.radius)

  # string representation of a circle
  def __str__ (self):
    return 'Center:' + self.center.__str__() + ' Radius: ' + str(self.radius)
    
  # test for equality of radius
  def __eq__ (self, other):
    tol = 1.0e-16
    return abs(self.radius - other.radius) < tol
   
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle

  def circle_circumscribes (self, r):
    x = (r.ul.x + r.lr.x)/2
    y = (r.ul.y + r.lr.y)/2
    center = Point(x,y)
    radius = center.dist(r.ul)
    new_circle = Circle(radius,x,y)
    return new_circle




class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  def length (self):
    return abs(self.ul.x - self.lr.x)

  # determine width of Rectangle (distance along the y axis)
  def width (self):
    return abs(self.ul.y - self.lr.y)

  # determine the perimeter
  def perimeter (self):
    return (self.length())*2 + (self.width())*2
    
  # determine the area
  def area (self):
    return (self.length()*self.width())

  # determine if a point is strictly inside the Rectangle
  def point_inside (self, p):
    return (self.ul.x < p.x < self.lr.x) and (self.ul.y > p.y >self.lr.y)

  # determine if another Rectangle is strictly inside this Rectangle
  def rectangle_inside (self, r):
    return self.point_inside(r.ul) and self.point_inside(r.lr)

  # determine if two Rectangles overlap (non-zero area of overlap)
  def does_intersect (self, other):
    return (other.lr.y > self.ul.y) or (other.lr.x < self.ul.x) or (other.ul.x > self.lr.x) or (other.ul.y < self.lr.y)

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  def rect_circumscribe (self, c):
    ul_x = c.center.x - c.radius 
    ul_y = c.center.y + c.radius
    lr_x = c.center.x + c.radius
    lr_y = c.center.y - c.radius
    new_rectangle = Rectangle(ul_x,ul_y,lr_x,lr_y)
    return new_rectangle

  # give string representation of a rectangle
  def __str__ (self):
    return 'UL: ' + self.ul.__str__() + ' LR: ' + self.lr.__str__()

  # determine if two rectangles have the same length and width
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs(self.length()-other.length())<tol and (abs(self.width()-other.width())<tol))



def main():
  # open the file geom.txt
 
  f = open('geom.txt', 'r')
  content = [line.rstrip('\n') for line in f]
  lines = [line.split(' ') for line in content]
  f.close()

  # create Point objects P and Q
  P = Point(float(lines[0][0]), float(lines[0][1]))
  Q = Point(float(lines[1][0]), float(lines[1][1]))

  # print the coordinates of the points P and Q
  print ('Coordinates of P:', P.__str__())
  print ('Coordinates of Q:', Q.__str__())

  # find the distance between the points P and Q
  print ('Distance between P and Q:', P.dist(Q))

  # create two Circle objects C and D
  circleC = Circle(float(lines[2][2]), float(lines[2][0]), float(lines[2][1]))
  circleD = Circle(float(lines[3][2]), float(lines[3][0]), float(lines[3][1]))

  # print C and D
  print ('Circle C:', circleC.__str__())
  print ('Circle D:', circleD.__str__())

  # compute the circumference of C
  print ('Circumference of C:', circleC.circumference())

  # compute the area of D
  print ('Area of D:', circleD.area())

  # determine if P is strictly inside C
  if circleC.point_inside(P) == True:
    print ('P is inside C')
  else:
    print ('P is not inside C')


  # determine if C is strictly inside D
  if circleD.circle_inside(circleC) == True:
    print ('C is inside D')
  else:
    print ('C is not inside D')

  # determine if C and D intersect (non zero area of intersection)
  if circleC.does_intersect(circleD) == True:
    print ('C does intersect D')
  else:
    print ('C does not intersect D')

  # determine if C and D are equal (have the same radius)
  if circleC.__eq__(circleD) == True:
    print ('C is equal to D')
  else:
    print ('C is not equal to D')

  # create two rectangle objects G and H
  G = Rectangle(float(lines[4][0]), float(lines[4][1]), float(lines[4][2]), float(lines[4][3]))
  H = Rectangle(float(lines[5][0]), float(lines[5][1]), float(lines[5][2]), float(lines[5][3]))

  # print the two rectangles G and H
  print ('Rectangle G', G.__str__())
  print ('Rectangle H', H.__str__())

  # determine the length of G (distance along x axis)
  print ('Length of G:', G.length())

  # determine the width of H (distance along y axis)
  print ('Width of H:', H.width())

  # determine the perimeter of G
  print ('Perimeter of G:', G.perimeter())

  # determine the area of H
  print ('Area of H:', H.area())

  # determine if point P is strictly inside rectangle G
  if G.point_inside(P) == True:
    print ('P is inside G')
  else:
    print ('P is not inside G')
 

  # determine if rectangle G is strictly inside rectangle H
  if H.rectangle_inside == True:
    print ('G is inside H')
  else:
    print ('G is not inside H')
  

  # determine if rectangles G and H overlap (non-zero area of overlap)
  if H.does_intersect(G) == True:
    print ('G does not overlap H')
  else:
    print ('G does overlap H')
 

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  my_circle = circleC.circle_circumscribes(G)
  print ('Circle that circumscribes G:', my_circle.__str__())

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  my_rectangle = G.rect_circumscribe(circleD)
  print ('Rectangle that circumscribes D:', my_rectangle.__str__())

  # determine if the two rectangles have the same length and width
  if G.__eq__(H) == True:
    print ('Rectangle G is equal to H')
  else:
    print ('Rectangle G is not equal to H')


  # close the file geom.txt

main()