list=[1,2,3,4,5]

print(list)
print(len(list))
print(list[0:3])

if list :
  print("yesss it work ")
 
#change list items 
list[0]="hello"
print(list)
list[2:]="there"
list[2:]=['there']
list.append("how are you")
list.insert(0,'hehehe')
print(list)

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
