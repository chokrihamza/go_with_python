import math
# simple declaration
def sayHello(name):
  print(f'hello {name}')

sayHello('Joe')
# with arbitrary arguments
def sayHello(*args):
  for i in args:
    print(f"hi {i}")
  else:
    print('now byyyyeeeee')
sayHello('alex','chris','doe')
# with keyword arguments 
def sayHello(**kvars):
  for key,val in kvars.items():
    print(f"Your {key}:{val}")
  else:
    print('now byyyyeeeee')

sayHello(name="aaaa",lastname="bbbbb")

# recursion
# the fibonacci serie
def Fibonacci(n):
    if n<= 0:
        return ("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(6))

# calculate the slope of a function

def slope(epsilon,point,func):
  func(point+epsilon)-func(point)/epsilon
  print((func(point+(epsilon/1000))-func(point))/(epsilon/1000))
    
slope(0.000000001,0,lambda x:math.exp(x))