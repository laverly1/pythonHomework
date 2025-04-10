class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print("nyam-nyam-nyam ... I'm eating")
    
    def walk(self):
        print("I'm walking, get out!")
    
    def sleep(self):
        print("stfu, I'm sleeping")

    def __str__(self):
        return f"My name is {self.name}, I'm {self.age} years old, I'm a {self.gender}"

class Cow(Animal):
    def __init__(self, name, age, gender, voice):
        super().__init__(name, age, gender)
        self.voice = voice

    def eat(self):
        print("Mooo ... I'm eating wood")
    
    def give_milk(self):
        print("Why everyone drinks my milk, but no one call me mum (")


class Dog(Animal):
    def __init__(self, name, age, gender, voice):
        super().__init__(name, age, gender)
        self.voice = voice

    def eat(self):
        print(f"{self.voice}, I cant find my bone, i digged it somewhere hereee...")

    def govern(self):
        print("I govern the home, no one come in!")

class Chicken(Animal):
    def __init__(self, name, age, gender, voice):
        super().__init__(name, age, gender)
        self.voice = voice
    
    def eat(self):
        print(f"{self.voice}, I eat corn, but I gotta be carefull of dog")

    
    def lay_egg(self):
        print("Unless I lay two eggs per day, my boss will send me to KFC")

dog1 = Dog("Rex", 3, "male", "Wuf-Wuf")
chicken1 = Chicken("Clucky", 2, "female", "Bawk-Bawk")


print(dog1)
dog1.eat()
dog1.govern()

print(" ")

print(chicken1)
chicken1.eat()
chicken1.lay_egg()