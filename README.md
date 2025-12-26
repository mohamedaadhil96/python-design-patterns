# Python Design Patterns

A collection of classic Gang of Four (GoF) design patterns implemented in Python. This repository aims to provide clear, practical examples to help understand and apply design patterns effectively.

Each pattern is placed in its own directory containing the implementation (Python scripts or Jupyter notebooks).

## Table of Contents

### Creational Patterns
- [Builder Pattern](Builder%20Pattern/)
- [Factory Pattern](Factory%20Pattern/)
- [Singleton Pattern](Singleton%20Pattern/)

### Structural Patterns
- [Adapter Pattern](Adapter%20Pattern/)

### Behavioral Patterns
- [Observer Pattern](Observer%20Pattern/)
- [Strategy Pattern](Strategy%20Pattern/)

## Creational Patterns

These patterns deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

- **[Builder Pattern](Builder%20Pattern/)**: Separates the construction of a complex object from its representation.
- **[Factory Pattern](Factory%20Pattern/)**: Defines an interface for creating an object, but lets subclasses decide which class to instantiate.
- **[Singleton Pattern](Singleton%20Pattern/)**: Ensures a class has only one instance and provides a global point of access to it.

## Structural Patterns

These patterns deal with class and object composition.

- **[Adapter Pattern](Adapter%20Pattern/)**: Allows incompatible interfaces to work together by wrapping an existing class with a new interface.

## Behavioral Patterns

These patterns are concerned with communication between objects.

- **[Observer Pattern](Observer%20Pattern/)**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.
- **[Strategy Pattern](Strategy%20Pattern/)**: Enables selecting an algorithm at runtime by encapsulating a family of algorithms.

## How to Run the Examples

Navigate to any pattern directory and run the main script (if present) or open the Jupyter notebook:

```bash
cd "Builder Pattern"
python main.py  # or open the .ipynb file in Jupyter
