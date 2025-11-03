#list methods 
#append method in list
fruits=["apple","banana"]
fruits.append("cherry")
print("appending: ",fruits)
#insert method in list
fruits=["apple","banana"]
fruits.insert(0,"cherry")
print("insert: ",fruits)

fruits=["apple","banana"]
fruits.insert(1,"cherry")
print("insert: ",fruits)
#extend method in list
fruits=["apple","banana"]
fruits.extend(["cherry","grapes"])
print("extend: ",fruits)
#remove() method in list
fruits=["apple","banana","grapes","banana","orange"]
fruits.remove("banana")
print("remove: ",fruits)
#pop() methos in list
fruits=["apple","banana","cherry"]
fruits.pop(1)
print("pop: ",fruits)
#clear() methods in list
fruits=["apple","banana","cherry"]
fruits.clear()
print("clear: ",fruits)
#index() methods in list
fruits=["apple","banana","cherry","banana"]
print("index value: ",fruits.index("banana"))
#count() method in list
fruits=["apple","banana","cherry","banana"]
print("count: ",fruits.count("banana"))
#sort() method in list for num
num=[4,5,3,2,1,1.98]
num.sort()
print("sort: ",num)
#sort() method in list for letters
fruits=["apple","orange","cherry","APPLE","banana"]
fruits.sort()
print("sort: ",fruits)
#reverse() method in list
num=[1,2,3,4,5,6]
num.reverse()
print("reverse: ",num)