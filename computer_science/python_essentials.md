# Decorator

A decorator in Python is a function (or callable) that modifies the behavior of another function, method, or class without changing its source code. E.g. `say_hi = my_decorator(my_function)`

Common built-in decorators:

- @staticmethod -> method does not use self or cls
- @classmethod -> method receives cls
- @property -> access a method like an attribute
- @dataclass -> auto-generates boilerplate code

```
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hi():
    print("Hi")

say_hi()
# Before function call
# Hi
# After function call
```

```
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()
```

```
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count

print(Counter.increment())
print(Counter.increment())

# 1
# 2
```

```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
print(r.area)

# 12
```

```
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(2, 5)
print(p)
print(p.x, p.y)

# Point(x=2, y=5)
# 2 5

```

# Static Method

A static method in Python is a method defined inside a class that does not depend on an instance of the class or the class itself. It behaves like a regular function, but is grouped inside a class for logical organization.

```
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(2, 3)  # 5
```

# Tuple | List

| Feature             | List                | Tuple                          |
| ------------------- | ------------------- | ------------------------------ |
| Mutability          | Mutable             | Immutable                      |
| Syntax              | `[1, 2, 3]`         | `(1, 2, 3)`                    |
| Item assignment     | Allowed             | Not allowed                    |
| Append / remove     | Allowed             | Not allowed                    |
| Hashable            | No                  | Yes (if elements are hashable) |
| Can be dict key     | No                  | Yes                            |
| Memory usage        | Higher              | Lower                          |
| Creation speed      | Slower              | Faster                         |
| Iteration speed     | Slightly slower     | Slightly faster                |
| Typical use         | Dynamic collections | Fixed collections              |
| Safety from changes | No                  | Yes                            |

# Tuple

## Tuple of size 1

```
t = (1,)
```

# Heap | Stack | Namespace

- Heap:
  - Objects live on the heap (<class A>).
  - Arbitrary allocation and deallocation.
  - Objects can live as long as needed.
  - Requires a memory manager.
  - Slower than stack.
  - You grab any free chunk.
  - Order does not matter.
  - Objects are “heaped” together.
  - All Python objects.
  - Arbitrary lifetimes.
  - Managed by garbage collection / ref counting.
  - Objects are created anywhere, destroyed when unreferenced, not tied to call order.
- Stack:
  - First in, last out.
  - Function call frames.
  - Local variable references.
  - Execution state.
- If lifetime is tied to call scope -> stack
- If lifetime is independent of call scope -> heap
- Names live in namespace dictionaries (globals()["A"], globals()["x"]).

```
# stack
push frame
  push locals
pop locals
pop frame
```

# Annotations

- Do not increase execution speed.
- Only for readibility.

# Class

## Empty Class

```
class A:
    pass
```

```
class A:
    ...
```

## Inheritance

```
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()
```

```
class A:
    def __init__(self):
        self.a = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.b = 5

b = B()
b.a  # 10
b.b  # 5
```

# Set

- Set insertion is O(1).
- list(set) is O(n).

# Dict

- Dict insertion is O(1).

# String Pooling | Integer Caching | Booleans

```
a = "hello"
b = "hello"
a is b  # True

a = "".join(["he", "llo"])
b = "".join(["he", "llo"])

a == b  # True
a is b  # False, because created at runtime, i.e. built while the program is already running, not known in advance when Python compiles the code
```

```
a = 10
b = 10
a is b  # True
# works only for range -5 to 256
```

```
True is True  # True
False is False  # True
```

# Inheritance

```

```

# Singleton

```
class Singleton:
    _instance = None

    def __new__(cls, value):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

a = Singleton(10)
b = Singleton(5)

a.value  # 5
```
