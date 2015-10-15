#!/usr/bin/python -tt

import sys
from pprint import pprint

class Employee:
  'Common base class for all employees'
  empCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1

  def displayCount(self):
    print "Total Employee %d" % Employee.empCount

  def displayEmployee(self):
    print "Name : ", self.name,  ", Salary: ", self.salary

# Define a main() function that prints a little greeting.
def main():
  "This would create first object of Employee class"
  emp1 = Employee("Zara", 2000)
  "This would create second object of Employee class"
  emp2 = Employee("Manni", 5000)

  emp1.displayEmployee()
  emp2.displayEmployee()
  print "Total Employee %d" % Employee.empCount
  
  emp1.age = 7  # Add an 'age' attribute.
  pprint (vars(emp1))
  emp1.age = 8  # Modify 'age' attribute.
  pprint (vars(emp1))
  del emp1.age  # Delete 'age' attribute.
  pprint (vars(emp1))

  print Employee.__dict__
  print Employee.__module__
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
