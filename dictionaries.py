


mydict= dict(name= "yabb", age= 6, city = "texas")
print(mydict)

value = mydict["city"]
print(value)


mydict["email"] = "yabb@jfj.com"
print(mydict)


del mydict["age"]
print(mydict)

mydict.popitem()
print(mydict)

try:
    print(mydict["name"])
except:
    print("Error")
    
if "name" in mydict:
    print("correct")
else:
    print("in correct")
    
     
for key in mydict:
    print(key)
        
for key, value in mydict.items():
    print(key,value)

mydict_cpy = dict(mydict)
mydict_cpy["email"] = "khjkshjfk"
print(mydict)
print(mydict_cpy) 

#update

mydict1 = {"class":"12","no":"6"}
mydict.update(mydict1)
print(mydict) 

# keyword

mydict2 = {3:9, 4:16, 5:25}
print(mydict2)

value = mydict2[5]
print(value)

mytuple = (8,7)
mydict2 = {mytuple: 5}
print(mydict2)