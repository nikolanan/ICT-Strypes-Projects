# Design Patterns in Python

## 1 SOLID Design Principles

### Single Responsibility Principle (SRP)

**Definition:**
The Single Responsibility Principle states that a class should have only one reason to change, meaning it should have only one job or responsibility.

**Why It Should Be Used:**
By adhering to SRP, classes are easier to maintain, test, and understand. A class focused on a single responsibility is more cohesive and less prone to errors when changes occur.

It reduces the complexity of the class and avoids tight coupling between different functionalities.

### Open/Closed Principle (OCP)

**Definition:**
The Open-Closed Principle states that a class should be open for extension but closed for modification. This means you should be able to extend a class’s behavior without modifying its existing code.

**Why It Should Be Used:**
It helps to make the system more extensible and flexible.

New functionalities can be added without disturbing the existing system, reducing the chances of introducing bugs.

### Liskov Substitution Principle (LSP)

**Definition:**
The Liskov Substitution Principle states that objects of a base class should be replaceable with objects of derived classes without affecting the correctness of the program.

**Why It Should Be Used:**
It ensures that derived classes can be used interchangeably with their base class without introducing errors.

It makes code more flexible and extensible.

### Interface Segregation Principle (ISP)

**Definition:**
The Interface Segregation Principle states that no client should be forced to depend on methods it does not use. This means interfaces should be small and focused on a specific behavior.

**Why It Should Be Used:**
It promotes smaller, more specific interfaces that are easier to implement and understand.

It avoids the "fat" interface problem, where a class implementing an interface is forced to implement methods that are irrelevant.

### Dependency Inversion Principle (DIP)

**Definition:**
The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. It also states that abstractions should not depend on details, but details should depend on abstractions.

**Why It Should Be Used:**
It decouples high-level and low-level modules, making the system more flexible and easier to modify.

Changes in low-level modules are less likely to affect high-level modules.

It makes the system easier to maintain and test.

## 2 Builder Pattern

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

## 3 Factory Method Pattern


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

## 4 Prototype Pattern

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

## 5 Singleton Pattern

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

## 6 Adapter Pattern

**Definition:**
The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to work together by wrapping an existing class with a new interface.

**Usage:**

You want to use an existing class, but its interface does not match the one you need.

You want to create a reusable class that cooperates with unrelated or unforeseen classes.

```python
class EuropeanSocket:
    def plug_in(self):
        return "Power from European socket"

class USASocketInterface:
    def connect(self):
        pass

class Adapter(USASocketInterface):
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def connect(self):
        return self.european_socket.plug_in()

# Usage
euro_socket = EuropeanSocket()
adapter = Adapter(euro_socket)
print(adapter.connect())  # Output: Power from European socket
```

## 7 Bridge Pattern

**Definition:**
The Bridge Pattern is a structural design pattern that decouples an abstraction from its implementation so that the two can vary independently. It separates the object’s interface from its implementation.

**Usage:**

You want to avoid a permanent binding between an abstraction and its implementation.

Both the abstractions and their implementations should be extensible independently.

You want to share an implementation among multiple objects.

```python
class Renderer:
    def render_circle(self, radius):
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} with vector graphics"

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} with pixels"

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        return self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

# Usage
raster = RasterRenderer()
circle = Circle(raster, 5)
print(circle.draw())  # Output: Drawing a circle of radius 5 with pixels
```

## 8 Composite Pattern

**Definition:**
The Composite Pattern is a structural design pattern that allows you to compose objects into tree structures to represent part-whole hierarchies. This lets clients treat individual objects and compositions of objects uniformly.

**Usage:*

You want to treat individual objects and groups of objects in the same way.

You want to represent part-whole hierarchies (like a document with sections, or a UI with containers and components).

You want to simplify client code by using a unified interface for all objects in the hierarchy.

```python
class GraphicObject:
    def __init__(self, name='Group'):
        self.name = name
        self.children = []

    def __str__(self, depth=0):
        result = ' ' * depth + self.name + '\n'
        for child in self.children:
            result += child.__str__(depth + 2)
        return result

class Circle(GraphicObject):
    def __init__(self):
        super().__init__('Circle')

class Square(GraphicObject):
    def __init__(self):
        super().__init__('Square')

# Usage
drawing = GraphicObject()
drawing.children.append(Circle())
drawing.children.append(Square())

group = GraphicObject()
group.children.append(Circle())
group.children.append(Square())

drawing.children.append(group)

print(drawing)
```

## 9 Decorator Pattern

**Definition:**
The Decorator Pattern is a structural design pattern that allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class.

**Usage:**

You want to add responsibilities to objects at runtime.

You want to avoid subclassing for extending functionality.

You want to keep each decorator class focused on a single responsibility.

```python
class Shape:
    def __str__(self):
        return ""

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"A circle of radius {self.radius}"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"A square with side {self.side}"

class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"

# Usage
circle = Circle(5)
red_circle = ColoredShape(circle, "red")

print(red_circle)
```

## 10 Facade Pattern

**Definition:**
The Facade Pattern is a structural design pattern that provides a simplified interface to a larger body of code, such as a complex subsystem. It hides the complexities of the system and provides a unified interface to the client.

**Usage:**

You want to provide a simple interface to a complex subsystem.

You want to decouple a client from the implementation details of subsystems.

You want to reduce dependencies between clients and subsystems.

```python
class CPU:
    def freeze(self):
        print("Freezing processor")

    def jump(self, position):
        print(f"Jumping to {position}")

    def execute(self):
        print("Executing instructions")

class Memory:
    def load(self, position, data):
        print(f"Loading data '{data}' to position {position}")

class HardDrive:
    def read(self, lba, size):
        print(f"Reading {size} bytes from sector {lba}")
        return "OS Boot Data"

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        data = self.hard_drive.read(0, 1024)
        self.memory.load(0, data)
        self.cpu.jump(0)
        self.cpu.execute()

# Usage
computer = Computer()
computer.start()
```

## 11 Flyweight Pattern

**Definition:**
The Flyweight Pattern is a structural design pattern that allows programs to support a large number of fine-grained objects efficiently by sharing common parts of state between them, instead of storing all data in every object.

**Usage:**

When many objects must be created that share common data to reduce memory usage.

Useful in situations where object instantiation is costly, and many instances are similar (e.g., text editors, game objects).

```python
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"Drawing {self.name} tree at ({x}, {y}) with color {self.color} and texture {self.texture}")


class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]


class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        self.trees.append(Tree(x, y, tree_type))

    def draw(self):
        for tree in self.trees:
            tree.draw()


# Usage
forest = Forest()
forest.plant_tree(1, 2, "Oak", "Green", "Rough")
forest.plant_tree(3, 4, "Oak", "Green", "Rough")
forest.plant_tree(5, 6, "Pine", "Dark Green", "Smooth")
forest.draw()
```

## 12 Proxy Pattern

**Definition:**
The Proxy Pattern is a structural design pattern that provides a surrogate or placeholder object to control access to another object. It acts as an intermediary between the client and the real object to add functionalities like access control, logging, lazy initialization, etc.

**Usage:**

When you need to control access to an object (e.g., based on user permissions).

To delay the creation and initialization of expensive objects.

To add logging, caching, or other cross-cutting concerns without modifying the actual object.

```python
class RealInternet:
    def connect_to(self, server_host):
        print(f"Connecting to {server_host}")


class InternetProxy:
    def __init__(self):
        self._real_internet = RealInternet()
        self._banned_sites = ['banned.com', 'blocked.net']

    def connect_to(self, server_host):
        if server_host in self._banned_sites:
            print(f"Access Denied to {server_host}")
        else:
            self._real_internet.connect_to(server_host)


# Usage
internet = InternetProxy()
internet.connect_to("example.com")  # Allowed
internet.connect_to("banned.com")   # Blocked
```

## 13 Chain of Responsibility Pattern

**Definition:**
The Chain of Responsibility Pattern is a behavioral design pattern in which a request is passed along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain.

**Usage:**

When you want to decouple the sender of a request from its receivers.

When multiple objects might handle a request, and the handler isn't known beforehand.

To build flexible systems that can dynamically change the chain at runtime.

```python
class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None


class AuthHandler(Handler):
    def handle(self, request):
        if request.get("user") == "admin":
            print("AuthHandler: User authenticated.")
            return super().handle(request)
        else:
            print("AuthHandler: Authentication failed.")
            return "Access denied"


class LoggingHandler(Handler):
    def handle(self, request):
        print(f"LoggingHandler: Logging access by {request.get('user')}")
        return super().handle(request)


class DataHandler(Handler):
    def handle(self, request):
        print("DataHandler: Handling data request.")
        return "Data served"


# Setup chain
auth = AuthHandler()
log = LoggingHandler()
data = DataHandler()

auth.set_next(log).set_next(data)

# Usage
response = auth.handle({"user": "admin"})
print("Response:", response)

response = auth.handle({"user": "guest"})
print("Response:", response)

```

## 14 Command Pattern

**Definition:**
The Command Pattern is a behavioral design pattern that turns a request into a stand-alone object containing all information about the request. This allows parameterizing objects with operations, queuing of operations, and logging the history of executed operations.

**Usage:**

When you want to parameterize objects with operations.

To support undo/redo functionality.

When you need to queue or log requests.

```python
class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()


class RemoteControl:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            self.history.pop().undo()


# Usage
light = Light()
remote = RemoteControl()

on_command = LightOnCommand(light)
off_command = LightOffCommand(light)

remote.execute_command(on_command)   # Light is ON
remote.execute_command(off_command)  # Light is OFF

remote.undo_last()                   # Light is ON
```

## 15 Interpreter Pattern

**Definition:**
The Interpreter Pattern is a behavioral design pattern that defines a representation for a grammar and provides a way to interpret sentences in that language. It is often used to interpret expressions in simple languages.

**Usage:**

When you have a language to interpret and you can represent its grammar using classes.

Useful for interpreting mathematical expressions, regular expressions, or domain-specific languages.

```python
class Expression:
    def interpret(self, context):
        pass


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)


# Usage
expression = Add(Number(5), Subtract(Number(10), Number(3)))
result = expression.interpret({})
print(result)  # Output: 12

```

## 16 Iterator Pattern

**Definition:**
The Iterator Pattern is a behavioral design pattern that provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

**Usage:**

When you need to traverse a collection without exposing its internal structure.

To provide a standard interface for iteration across different container types.

## 17 Mediator Pattern

**Definition:**
The Mediator Pattern is a behavioral design pattern that defines an object (the mediator) that encapsulates how a set of objects interact. It promotes loose coupling by preventing objects from referring to each other explicitly, allowing their interaction to be altered independently.

**Usage:**

When multiple objects communicate in a complex but well-defined way.

To centralize complex communications and control logic in one place.

To reduce dependencies between communicating components (e.g., in GUIs or chat systems).

```python
class ChatRoom:
    def show_message(self, user, message):
        print(f"[{user.name}]: {message}")


class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom

    def send(self, message):
        self.chatroom.show_message(self, message)


# Usage
room = ChatRoom()
john = User("John", room)
jane = User("Jane", room)

john.send("Hi Jane!")
jane.send("Hello John!")
```

## 18 Memento Pattern

**Definition:**
The Memento Pattern is a behavioral design pattern that allows an object to capture and externalize its internal state so that it can be restored later, without violating encapsulation.

**Usage:**

To implement undo/redo functionality.

When you need to persist and restore the state of an object.

```python
class Memento:
    def __init__(self, state):
        self.state = state


class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        print(f"Setting state to: {state}")
        self._state = state

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.state
        print(f"Restored state to: {self._state}")


class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


# Usage
originator = Originator()
caretaker = Caretaker()

originator.set_state("State #1")
caretaker.add_memento(originator.save())

originator.set_state("State #2")
caretaker.add_memento(originator.save())

originator.set_state("State #3")
originator.restore(caretaker.get_memento(0))  # Restores to "State #1"

```

## 19 Observer Pattern

**Definition:**
The Observer Pattern is a behavioral design pattern that allows an object (known as the subject) to notify a list of dependent objects (known as observers) automatically of any state changes, typically by calling one of their methods.

**Usage:**

When you want multiple objects to listen to the state changes of another object without tight coupling between them.

Commonly used in event-driven systems or UI frameworks.

```python
class Observer:
    def update(self, message):
        raise NotImplementedError("Subclass must implement abstract method")


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Observer {self.name} received message: {message}")


class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# Usage
subject = Subject()

observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("Hello, observers!")

subject.remove_observer(observer1)
subject.notify_observers("Goodbye, Observer 1!")

```

## 20 State Pattern

**Definition:**
The State Pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. The object will appear to change its class, meaning it can transition between states without modifying the object's code directly.

**Usage:**

When an object's behavior depends on its state and it must change its behavior at runtime.

Commonly used in finite state machines, where different behaviors are triggered based on the object's state.

```python
class State:
    def handle(self):
        raise NotImplementedError("State class must implement handle method.")


class ConcreteStateA(State):
    def handle(self):
        print("State A: Performing action A.")


class ConcreteStateB(State):
    def handle(self):
        print("State B: Performing action B.")


class Context:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def request(self):
        if self.state:
            self.state.handle()


# Usage
context = Context()

# Initially in State A
state_a = ConcreteStateA()
context.set_state(state_a)
context.request()  # Output: State A: Performing action A.

# Now change to State B
state_b = ConcreteStateB()
context.set_state(state_b)
context.request()  # Output: State B: Performing action B.

```

## 21 Starategy Pattern

**Definition:**
The Strategy Pattern is a behavioral design pattern that enables a client to choose from a family of algorithms or strategies to perform a task. It allows the algorithm to be selected at runtime, making it easy to switch between different methods of solving the same problem without modifying the client code.

**Usage:**

When there are multiple ways of performing an operation (algorithm), but the specific method can vary depending on the context.

Useful for situations where algorithms may change based on user input, environment, or other conditions.

```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        print(f"Strategy A: Processing data: {data}")


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        print(f"Strategy B: Processing data: {data}")


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        self._strategy.execute(data)


# Usage
context = Context(ConcreteStrategyA())  # Initially using Strategy A
context.execute_strategy("input data")  # Output: Strategy A: Processing data: input data

# Change to Strategy B at runtime
context.set_strategy(ConcreteStrategyB())
context.execute_strategy("input data")  # Output: Strategy B: Processing data: input data

```

## 22 Template Method Pattern

**Definition:**
The Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in the base class, but lets subclasses implement specific steps of the algorithm. The pattern allows the steps of the algorithm to be customized without changing the overall structure of the algorithm.

**Usage:**

When you have an algorithm with multiple steps that can be shared across different implementations, but some of the steps need to be customized by subclasses.

Helps in reducing code duplication by allowing common steps to be implemented once and leaving variation points to be implemented by subclasses.

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    def step3(self):
        print("Step 3: Finalizing the process.")

class ConcreteClassA(AbstractClass):
    def step1(self):
        print("ConcreteClassA: Performing step 1.")

    def step2(self):
        print("ConcreteClassA: Performing step 2.")

class ConcreteClassB(AbstractClass):
    def step1(self):
        print("ConcreteClassB: Performing step 1.")

    def step2(self):
        print("ConcreteClassB: Performing step 2.")

# Usage
concrete_a = ConcreteClassA()
concrete_a.template_method()
# Output:
# ConcreteClassA: Performing step 1.
# ConcreteClassA: Performing step 2.
# Step 3: Finalizing the process.

concrete_b = ConcreteClassB()
concrete_b.template_method()
# Output:
# ConcreteClassB: Performing step 1.
# ConcreteClassB: Performing step 2.
# Step 3: Finalizing the process.

```


## 23 Visitor Pattern

**Definition:**
The Visitor Pattern is a behavioral design pattern that allows you to add further operations to objects without having to modify them. It involves creating a new class of visitors that can "visit" different types of objects and execute specific operations on them. This pattern is useful when you need to perform operations on objects of different types in a flexible and extensible way.

**Usage:**

When you need to perform operations on a set of objects with different types and you don't want to modify the classes of those objects.

To avoid cluttering classes with unrelated behavior that is only relevant in certain contexts.

When operations on objects are subject to change frequently, but the object structure remains the same.

```python
from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"ConcreteVisitor1: Visiting {element.__class__.__name__}.")

    def visit_concrete_element_b(self, element):
        print(f"ConcreteVisitor1: Visiting {element.__class__.__name__}.")

class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"ConcreteVisitor2: Visiting {element.__class__.__name__}.")

    def visit_concrete_element_b(self, element):
        print(f"ConcreteVisitor2: Visiting {element.__class__.__name__}.")

# Client code
elements = [ConcreteElementA(), ConcreteElementB()]

visitor1 = ConcreteVisitor1()
visitor2 = ConcreteVisitor2()

# Visiting elements using different visitors
for element in elements:
    element.accept(visitor1)

print("\n---")

for element in elements:
    element.accept(visitor2)
```