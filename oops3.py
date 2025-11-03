class animal:
    def sound001(self):
        print("Animal makes sound")
    
class dog(animal):
    def sound(self):
        print("dog barks")

class cat(dog):
    def sound01(self):
        print("cat meow")
    
d = cat()
d.sound001()
d.sound()
d.sound01()
