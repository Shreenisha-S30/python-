#you and your friend went shopping.
# your list: {"milk","bread","eggs","butter"} 
# friend's list: {"bread","butter","jam","cheese"}
#write a python program to find: items both of you bought, items only you bought, intem only your friend bought, the list of all unique items
my_list= {"milk","bread","eggs","butter"} 
frd_list= {"bread","butter","jam","cheese"}
print(my_list.intersection(frd_list))
print(my_list.difference(frd_list))
print(frd_list.difference(my_list))
print(my_list.union(frd_list))