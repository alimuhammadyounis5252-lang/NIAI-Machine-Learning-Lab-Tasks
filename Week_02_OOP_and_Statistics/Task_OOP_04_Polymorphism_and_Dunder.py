# Week 2 - OOP Task 4: Polymorphism, Operator Overloading & Dunder Methods
# Student Name: Ali Muhammad Younis (886)

print("=" * 60)
print(" OOP Task 4: Polymorphism & Dunder (Magic) Methods")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Dynamic Polymorphism (Common Interface)
class LossFunction:
    def compute(self, y_true, y_pred):
        raise NotImplementedError("Subclasses must implement compute()")

class MeanSquaredError(LossFunction):
    def compute(self, y_true, y_pred):
        return sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / len(y_true)

class MeanAbsoluteError(LossFunction):
    def compute(self, y_true, y_pred):
        return sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

# Polymorphic runner
def print_loss_evaluation(criterion: LossFunction, y_true, y_pred):
    print(f"Loss with {criterion.__class__.__name__}: {criterion.compute(y_true, y_pred):.4f}")

y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5, 0.0, 2.0, 8.0]

print("\n--- 1. Dynamic Polymorphism Demonstration ---")
print_loss_evaluation(MeanSquaredError(), y_true, y_pred)
print_loss_evaluation(MeanAbsoluteError(), y_true, y_pred)

# 2. Operator Overloading with Magic / Dunder Methods
class FeatureVector:
    def __init__(self, elements):
        self.elements = list(elements)

    # __str__: Human-readable representation
    def __str__(self):
        return f"FeatureVector({self.elements})"

    # __repr__: Formal representation
    def __repr__(self):
        return f"FeatureVector(elements={self.elements})"

    # __len__: Support for len(vec)
    def __len__(self):
        return len(self.elements)

    # __add__: Vector addition (+)
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be equal in length for addition")
        return FeatureVector([a + b for a, b in zip(self.elements, other.elements)])

    # __eq__: Vector equality (==)
    def __eq__(self, other):
        return self.elements == other.elements

print("\n--- 2. Operator Overloading & Dunder Methods ---")
v1 = FeatureVector([1.0, 2.0, 3.5])
v2 = FeatureVector([4.0, 5.0, 1.5])
v3 = v1 + v2

print("v1:", v1)
print("v2:", v2)
print("v1 + v2 (overloaded +):", v3)
print("Length of v3:", len(v3))
print("Is v1 == v2?", v1 == v2)
print("Is v1 == FeatureVector([1.0, 2.0, 3.5])?", v1 == FeatureVector([1.0, 2.0, 3.5]))
