#example set
fruits={"apple","banana"}
fruits.add("mango")
fruits.add("apple")
print(fruits)
#add method 
fruits={"apple","banana","cherry"}
fruits.add("mango")
print(fruits)
#update ,ethod
fruits={"apple","banana","cherry"}
fruits.update(["mango","grapes"])
print(fruits)
#remove method
fruits={"apple","banana","cherry"}
fruits.remove("banana")
print(fruits)
#intersection method
a={2,4,5}
b={4,2,3}
print(a.intersection(b))
#union method
a={2,4,5}
b={1,2,3}
print(a.union(b))
#difference method it consider only set one
a={2,4,5}
b={1,2,4}
print(a.difference(b))