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