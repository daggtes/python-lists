# tuple is a collection of datatype that can't be altered objects that long togther
mytuple = tuple(["max", 8, "lisbon"])
print(mytuple)

item= mytuple[-1]
print(item)

for c in mytuple:
    print(c)
    
if "max" in mytuple:
    print("ok")
else:
    print("not ok")
    
print(len(mytuple))
print(mytuple.count(8))
print(mytuple.index(8))

# slicing 

b =  (4, 5, 6, 7, 8, 9, 10, 11, 12)
a = b[4:7]
print(a)

# packaging

name, age, city = mytuple
print(name, age, city)

# unpacking

i2, *i3, i4 = b
print(i2)
print(i3)
print(i4)


