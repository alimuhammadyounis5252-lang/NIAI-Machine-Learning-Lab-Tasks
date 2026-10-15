# Week 2 - OOP Task 5: Advanced OOP, Abstract Classes, Dataclass, Composition
# Student Name: Ali Muhammad Younis (886)

from abc import ABC, abstractmethod
from dataclasses import dataclass

print("=" * 60)
print(" OOP Task 5: Abstract Base Class, Dataclass & Composition")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Abstract Base Class (ABC)
class AbstractModel(ABC):
    @abstractmethod
    def forward(self, x):
        """Pass input through model."""
        pass

    @abstractmethod
    def backward(self, grad):
        """Backpropagate gradients."""
        pass

class SimplePerceptron(AbstractModel):
    def forward(self, x):
        return f"Perceptron activation for input {x}"

    def backward(self, grad):
        return f"Perceptron gradient adjusted with {grad}"

print("\n--- 1. Abstract Base Class Verification ---")
model = SimplePerceptron()
print(model.forward([0.5, 0.2]))
print(model.backward(0.01))

# 2. Empty Class (Placeholder / Marker Pattern)
class ModelCheckpoint:
    pass

checkpoint = ModelCheckpoint()
checkpoint.epoch = 10
checkpoint.val_loss = 0.231
print("\n--- 2. Empty Class Dynamic Attributes ---")
print(f"Checkpoint saved at epoch {checkpoint.epoch} with val_loss {checkpoint.val_loss}")

# 3. Data Class (@dataclass)
@dataclass
class Hyperparameters:
    learning_rate: float
    batch_size: int
    epochs: int
    optimizer: str = "Adam"

hp = Hyperparameters(learning_rate=0.001, batch_size=32, epochs=50)
print("\n--- 3. Dataclass Representation ---")
print("Hyperparameters:", hp)

# 4. Inner / Nested Class
class DeepNetwork:
    class WeightsInitializer:
        @staticmethod
        def xavier_init():
            return "Xavier (Glorot) Initialization applied"

    def __init__(self):
        self.initializer = self.WeightsInitializer()

network = DeepNetwork()
print("\n--- 4. Inner Class Access ---")
print(network.initializer.xavier_init())

# 5. Composition vs Aggregation
# Composition: Part cannot exist without the whole
# Aggregation: Part has an independent lifecycle
class CPU:
    def __init__(self, cores: int):
        self.cores = cores

class TrainingServer:
    def __init__(self, server_name: str, cpu_cores: int, external_gpu=None):
        self.server_name = server_name
        self.cpu = CPU(cpu_cores)          # Composition: CPU belongs to server
        self.external_gpu = external_gpu    # Aggregation: GPU can be swapped/shared

print("\n--- 5. Composition & Aggregation ---")
server = TrainingServer("AI-Cluster-Node-01", 16, external_gpu="NVIDIA A100")
print(f"Server {server.server_name} has {server.cpu.cores} CPU cores and {server.external_gpu} GPU.")
