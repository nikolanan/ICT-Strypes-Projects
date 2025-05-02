# Design Patterns in Python

## 1 Builder Pattern

**Definition**:
The Builder Pattern is a way to build complex objects step-by-step. It separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

**Usage**:
Separates construction logic from the object.

Lets you chain methods to set attributes.

You can enforce certain build steps (like “name must be set before building”).

### Example:

```python
class Person:
    def __init__(self):
        self.name = None
        self.position = None

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def called(self, name):
        self.person.name = name
        return self

    def works_as(self, position):
        self.person.position = position
        return self

    def build(self):
        return self.person
```

## 2 Factory Method Pattern


**Definition**:
The Factory Pattern is a creational design pattern that provides a way to create objects without exposing the instantiation logic (like using __init__ directly). Instead, it uses a factory method (often a function or static method) to create and return the right object.

**Usage**:
You don't want the user to use ClassName() directly.

The creation might vary based on input.

You're returning different subclasses depending on the need.

### Example:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")
```

## 3 Prototype Pattern

**Definition**: 
The Prototype Pattern is a creational design pattern that allows you to create new objects by copying (cloning) existing ones, instead of creating them from scratch.

**Usage**:
Objects that are expensive to create (e.g. deep initialization, DB connections, etc.)

Objects that require many steps to configure

A need to create many similar objects with slight changes

#### Example:

```python
import copy

class Sheep:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name} the {self.color} sheep"

    def clone(self):
        return copy.deepcopy(self)

original = Sheep("Dolly", "white")

cloned = original.clone()
cloned.name = "Molly"

print(original)  
print(cloned)   
```

## 4 Singleton Pattern

**Definition**:
The Singleton Pattern is a design pattern that restricts the instantiation of a class to one single instance. This is useful when exactly one object is needed to coordinate actions across the system.

**Usage**:
Only one instance of a class is needed.

You want to control access to a shared resource (like a database connection or a configuration object).

### Example:

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance...")
            cls._instance = super().__new__(cls)
        return cls._instance
```


