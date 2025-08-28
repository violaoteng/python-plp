class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method!")


class Dog(Animal):
    def move(self):
        return "Running"


class Fish(Animal):
    def move(self):
        return "Swimming"


class Bird(Animal):
    def move(self):
        return "Flying "


# Example usage
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    print(animal.move())
