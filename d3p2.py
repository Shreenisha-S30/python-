#example for dictionary
student={"name":"ravi","age":21,"course":"BBA"}
print(student.keys())  #keys()
print(student.values()) #values()
print(student.items()) #items()
print(student.get("name","arun")) #get()
student.update({"grade":"A"})
print(student)
student.pop("age")
print(student)
student.clear()
print(student)

#create a dictionary of 3 subjects and marks
marks = {"maths":90,"Science":85,"english":88}
print(marks.items())
marks.popitem()
print(marks)