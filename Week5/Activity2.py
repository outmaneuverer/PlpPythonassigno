class Animal:
    def move(self):
        print("This animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")

class Bird(Animal):
    def move(self):
        print("The bird flies 🐦")

animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()  
