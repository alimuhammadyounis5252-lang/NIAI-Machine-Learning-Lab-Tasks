# Week 2 - OOP Task 1: Classes, Objects, Variables, and Methods
# Student Name: Ali Muhammad Younis (886)

print("=" * 60)
print(" OOP Task 1: Classes, Instance/Class Variables & Methods")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

class NeuralLayer:
    # Class Variable (Shared across all instances)
    layer_count = 0
    default_activation = "ReLU"

    def __init__(self, name: str, units: int, activation: str = None):
        # Instance Variables (Unique to each instance)
        self.name = name
        self.units = units
        self.activation = activation if activation else NeuralLayer.default_activation
        
        # Increment class counter
        NeuralLayer.layer_count += 1
        print(f"[Constructor] Created layer: {self.name} with {self.units} units")

    # Instance Method
    def get_info(self) -> str:
        return f"Layer '{self.name}': {self.units} units, Activation: {self.activation}"

    # Class Method
    @classmethod
    def set_default_activation(cls, new_act: str):
        cls.default_activation = new_act
        print(f"[Class Method] Default activation set to {new_act}")

    # Static Method (Independent utility function)
    @staticmethod
    def is_valid_unit_count(count: int) -> bool:
        return isinstance(count, int) and count > 0

    # Destructor
    def __del__(self):
        # Note: Destructor called upon garbage collection
        pass

# Demonstration
print("\n--- 1. Testing Static Method ---")
print("Is 64 valid units?", NeuralLayer.is_valid_unit_count(64))
print("Is -5 valid units?", NeuralLayer.is_valid_unit_count(-5))

print("\n--- 2. Instantiating Objects ---")
layer1 = NeuralLayer("Input_Dense", 128)
layer2 = NeuralLayer("Hidden_Dense", 64, activation="GELU")

print("\n--- 3. Calling Instance Methods ---")
print(layer1.get_info())
print(layer2.get_info())

print(f"\n--- 4. Class Variable Access ---")
print(f"Total layers created so far: {NeuralLayer.layer_count}")

NeuralLayer.set_default_activation("Swish")
layer3 = NeuralLayer("Output_Dense", 10)
print(layer3.get_info())
