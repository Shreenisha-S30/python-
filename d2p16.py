#you are going shopping
#start with a list: ["milk","bread","eggs"]
# add "butter" and "jam" to the list
# remove "bread" from the list
# sort the items alphabetically
# print the final shopping list
list=  ["milk","bread","eggs"]
print("Initial shopping list : ",list)
list.extend(["butter","jam"])
list.remove("bread")
list.sort()
print("Final shopping list is : ",list)