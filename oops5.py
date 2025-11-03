#example for encapsulation
class student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        self.__marks = marks
    
s1 = student("Rahul",80)
print("Marks:",s1.get_marks())

s1.set_marks(90)
print("Updated Marks:",s1.get_marks())