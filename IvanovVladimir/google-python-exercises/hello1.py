#!/usr/bin/python -tt

import sys
#!/usr/bin/python

class Point:
  def __init( self, x=0, y=0):
    self.x = x
    self.y = y
  def __del__(self):
    class_name = self.__class__.__name__
    print class_name, "destroyed"

# Define a main() function that prints a little greeting.
def main():
  pt1 = Point()
  pt2 = pt1
  pt3 = pt1
  print id(pt1), id(pt2), id(pt3) # prints the ids of the obejcts
  del pt1
  del pt2
  del pt3

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
