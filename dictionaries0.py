a="brand"
b="model"
c="year"
car = {
  a: "Ford",
  b: "Mustang",
  c: 1964
}

print(car,type(car),len(car))
print(car.get("brand"))
print(car.keys())
print(car.values())
print(car.items())
# nested dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print(myfamily.items())