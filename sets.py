set1={1,2,3}
print(set1,type(set1),len(set1))
(a,b,_)=set1
print(a,b)
# add and update in sets
# like in maths in sets we can and singletons {} or another set
set1.add(4)
print(set1)
set1.update([1,2,10,14,15]) # inside update we put a iterables 
print(set1)
# remove,discard,pop,clear
set1.remove(1)
print(set1)
set1.discard(2)
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)
# u can also use del
# like maths we have union,intersetion,update to add set etc

x={1,2,3}
y={5,57,7}
print(y.isdisjoint(x))
