# string function in python 
text="hello there {name}"
print(text.capitalize())
print(text.casefold())
print(text.center(50))
print(text.count('h'))
print(text.count('h',0,5))
print(text.encode())
print(text.endswith('e'))

print("h\te\tl\tl\to".expandtabs(12))
print(text.find('e'))
text="the price of this article is {price:.1%}"
print(text.format(price=0.20))
# format_map
print("""hello {name}, you buy
 {buy},that cost {price}""".format_map({"name":"hamza",
                                        "buy":"car",
                                        "price":200
                                        }))
print(text.index('h'))
text="hello120"
print(text.isalnum())
text="hello 120"
print(text.isalnum())
print("hello".isalpha())
print("hello10".isalpha())
print("\u0033".isdecimal(),"\u0047".isdecimal())
print("1230".isdigit(),"\u00B2".isdigit())
print('10name'.isidentifier(),'first var'.isidentifier(),'name'.isidentifier())
print('102name'.islower(),'Hello'.islower())
print("10203".isnumeric(),'\u0030'.isnumeric(),'-1'.isnumeric(),'dfdf1020'.isnumeric())
print("hello\n there".isprintable(),"hello\t there".isprintable())
print("hello\*& there".isprintable())
print("    ".isspace(),"a   ".isspace())
print('Hello And '.istitle(),'hello'.istitle())
print("HOLLA123".isupper())
dict={
  "car":'toyota',
  "price":200,
  "engine":"on V"
}

print(".".join(dict))
print(",".join(("1","2","3","4","5")))
print('hello'.ljust(20,'o')+"there")
print("HOLLA".lower())
print("abnhello".lstrip("abn"))
txt = "Hello Sam!"
mytable = txt.maketrans("S", "J",'Hello')
print(mytable)
print(txt.translate(mytable))
text="abcd"
print(text.partition('b')[2])
print("hello Sam".replace('Sam','Alex'))
print("hoello".rfind('o'))
print("    hello    ".strip())