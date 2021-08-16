# global vars are accessible inside and outside the function
#
number = 5


def add():
  print(number)


add()
print(number)

# in python local vars normally accessible only
#inside function but using the key "global " we
# can create a global var from inside a function

greeting = "good bye"


def myfunction():
  global greeting
  greeting = "hello there"
  print('hello there')


print(greeting)
myfunction()
print(greeting)
