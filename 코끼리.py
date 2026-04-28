class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
class Elephant(Animal):
    def speak(self):
        return f"{self.name} says Foo!"

my_dog = Dog(name="Buddy")
my_cat = Cat(name="Whiskers")
my_elephant = Elephant(name="Ally")

print(my_dog.speak())
print(my_cat.speak())
print(my_elephant.speak())