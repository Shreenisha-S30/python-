#example for encapsulation without using get and set method
class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks

    def __display_info(self):
        print("Name:",self.__name)
        print("Marks:",self.__marks)

    def show(self):
        print("Student detail:")
        self.__display_info()
    
s1 = Student("Rahul",80)
s1.show()
