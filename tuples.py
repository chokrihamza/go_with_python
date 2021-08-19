tup=(1,2,3,3)
tup=tuple((12,3,2,3))
print(tup,type(tup),len(tup))
# access tuple is the same as list access
if 12 in tup:
  print("yesss ")
  
# tuples are immutable
# tup[1]="fgjdfg" will generate an error

# note that tuples an unchangeable 

tuple1=(1,2,3,4,5,6)
tuple1+=("3ghj",)

print(tuple1)
# unpack a tuple and a list 
(a,b,c)=(1,2,3)
d,e,f=[4,5,6]
print(a,b,c,d,e,f)