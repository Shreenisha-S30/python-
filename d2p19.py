#two different course have student lists
# python class: {"Ravi","ankita","kiran","rahul"}
#java class: {"kiran","rahul","sneha","meena"}
#write a program to : find students who learning both, only python , only java, find all unique students from both classes
python= {"Ravi","ankita","kiran","rahul"}
java= {"kiran","rahul","sneha","meena"}
print("learning both: ",python.intersection(java))
print("only python: ",python.difference(java))
print("only java: ",java.difference(python))
print("unique students: ",python.union(java))