# main.py
from crochet import Crochet
from animals import Dog, Fish, Bird

# Assignment 1: Crochet
print(" Assignment 1: Crochet Class")
project1 = Crochet("Scarf", "Cotton", "Red", 5)
project2 = Crochet("Hat", "Wool", "Blue", 3)

print(project1)
print(project1.start_project())
print(project2.finish_project())

print("\n Activity 2: Polymorphism Challenge")
# Polymorphism with Animals
animals = [Dog(), Fish(), Bird()]
for animal in animals:
    print(animal.move())
