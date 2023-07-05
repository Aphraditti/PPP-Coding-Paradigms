# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(arr):
    flattened = [item for sublist in arr for item in sublist]  # Flattening the array
    sorted_arr = sorted(flattened)  # Sorting the flattened array in ascending order
    return sorted_arr


# 1. How does this solution ensure data immutability?
# This solution ensures data immutability by not modifying the original input array or any other external state. It creates a new list (flattened) using list comprehension and returns a sorted version of that new list. The original array remains unchanged throughout the process, preserving data immutability.

# 2. Is this solution a pure function? Why or why not?
# Yes, this solution is a pure function. It only depends on the input parameter arr and produces a result based solely on that input. It does not have any side effects or modify external state. The same input will always yield the same output, making it predictable and easy to reason about.

# 3. Is this solution a higher-order function? Why or why not?
# No, this solution is not a higher-order function. A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result. In this case, the flatten_and_sort function takes a single argument (arr) which is not a function itself.

# 4. Would it have been easier to solve this problem using a different programming style?
# The choice of programming style depends on the problem and the programmer's familiarity and preferences. While functional programming provides benefits such as immutability and pure functions, it may not always be the easiest or most intuitive approach for every problem. In this case, the problem of flattening and sorting an array of integers can be solved using different programming styles, such as imperative or object-oriented programming, which might offer more straightforward solutions depending on the specific requirements and constraints.

# 5. Why is functional programming a helpful paradigm when solving this problem?
# Functional programming is a helpful paradigm when solving this problem because it emphasizes immutability, pure functions, and the composition of functions. By adhering to these principles, the functional solution ensures that the original data is not modified, avoids side effects, and produces a predictable and reliable result. Functional programming also promotes code clarity and maintainability by breaking the problem into smaller, reusable functions that can be composed to solve complex tasks. This modular and declarative approach can lead to more concise and readable code, making it easier to understand and reason about the solution.


# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 


class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        self.condition = "repaired"


class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def flame_jet(self, podracer):
        podracer.condition = "trashed"


# Encapsulation: The solution encapsulates the attributes (max_speed, condition, price) and behavior (repair, boost, flame_jet) within the appropriate classes (Podracer, AnakinsPod, SebulbasPod). This allows for data hiding and ensures that the internal implementation details are hidden from the outside world.

# Abstraction: The classes provide a higher level of abstraction by representing real-world entities (podracers) with their attributes and behaviors. The user of the classes doesn't need to know the internal implementation details but can interact with the objects using the defined methods and attributes.

# Inheritance: The classes AnakinsPod and SebulbasPod inherit from the base class Podracer, which allows them to inherit its attributes and methods. This promotes code reuse and facilitates the creation of specialized subclasses that inherit common behavior while adding their own specific behavior.

# Polymorphism: Polymorphism is not explicitly demonstrated in this particular solution. However, it could be extended by overriding methods in the subclasses to provide different implementations while maintaining the same method signature as the base class.

# Regarding whether it would have been easier to implement this problem using a different coding style, it depends on the specific requirements and constraints. Object-Oriented Programming (OOP) is well-suited for modeling complex systems and organizing code around objects and their interactions. In this case, OOP provides a natural way to represent different types of podracer objects, define their specific behaviors, and encapsulate their data.

# The use of classes and inheritance allows for the creation of specialized subclasses (AnakinsPod, SebulbasPod) with their unique functionalities while inheriting the common attributes and methods from the base class (Podracer). This makes the code modular, extensible, and easier to maintain. The relationships between classes and the ability to define specialized behaviors are key advantages of OOP in solving this problem.