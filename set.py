from re import A


myset = {1, 2, 3, 1, 3}#duplication not allowded
print(myset)

#creating an empty set together with adding and deleting 
 
myset2= set()
myset2.add('hello')
myset2.add("you")
print(myset2.pop())
print(myset2)

# union and intersection 

odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

u= odds.union(even)
print(u)

i = odds.intersection(prime)
print(i)

# difference

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,}

diff = setA.difference(setB) 
print(diff) 

sy = setA.symmetric_difference(setB)
print(sy)

#super state 

print(setA.issuperset(setB)) 
print(setA.isdisjoint(setB))

# frozenset unable to update

a= frozenset([1,2,3,4])
print(a)