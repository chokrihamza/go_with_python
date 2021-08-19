ls=[1,2,3,4,5]

print(ls)
print(len(ls))
print(ls[0:3])

if ls :
  print("yesss it work ")
 
#change ls items 
ls[0]="hello"
print(ls)
ls[2:]="there"
ls[2:]=['there']
ls.append("how are you")
ls.insert(0,'hehehe')
print(ls)

list1=[1,2,3,4]
list2=["a","b","c","d"]
list1.extend(list2)
list1.remove("a")
#list1.clear()
print(list1)
i=0
while i<len(list1):
  print(list1[i])
  i=i+1
print([x for x in list1 if type(x)==int])
print([x for x in list1 if type(x)==str])
print([f"{x}{y}{z}{t}" for x in range(2) 
       for y in range(2)
       for z in range(2)
       for t in range(2)],sep="/")

x=[1,5,8,10,25,1,2,5,6,14,15]
x.sort(reverse=True)
print(x)
x.sort(key=lambda x:pow(x,2))
print(x)
# copy a list
y=x.copy()
print(y)
# or just like this 
a=[1,2,3]
y=list(a)
print(y)

# in python you can join lists 
listx=[1,2,3,4]
listy=['a','b','c']
print(listx+listy)
