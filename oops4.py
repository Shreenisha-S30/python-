class person:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print("Name: ",self.name)

class student(person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    def show(self):
        print("Grade: ",self.grade)

s1 = student("Shreenisha","A")
s1.display()
s1.show()