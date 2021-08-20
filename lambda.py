# the lambda functions 
# all functions in python are
# objects first class objects 
add=lambda x,y:(x+y) # add reference to that lambda first class object

add(5,3)
run_off=lambda x:print(x)
# we can pass a functions as params in python 
# because functions are objects and not!!! vice verca 
# i can use them as a callback functions 
# example
def add_and_print(sum,copy):
  copy(sum(10,10))
  
add_and_print(add,run_off)