#a="""hello there,how are you
#for me am fine,
#hope you are all good

#"""
#print(a)
#print(a[2:])

#for i in a:
#  print(i)
  
#print(len(a))
#print("hello" in a)
#print("hello" not in a)

a="hello there"
#slicing
print(a[0:5])
print(a[:5])
print(a[5:])
print(a[-5:-2])
#modifing
print(a.capitalize())
print(a.upper())
print(a.strip())
print(a.replace('h','ok'))
x,y=a.split(' ')
print(x)
print(y)
# combine string and number in python
age=25
text="hello there am {}"
print(text.format(age))

name="hamza"
age="26"
last_name="chokri"
text="hello,my name is {2},{1} ,am {0}"
print(text.format(name,age,last_name))