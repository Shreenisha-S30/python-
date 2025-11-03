#example for polymorphism
class dog:
    def sound(self):
        return "Bark"

class cat:
    def sound(self):
        return "Meow"
    
def make_sound(animal):
    print(animal.sound())

d = dog()
c = cat()

make_sound(d)
make_sound(c)