# Week 2 - OOP Task 3: Encapsulation, Access Specifiers, and Properties
# Student Name: Ali Muhammad Younis (886)

print("=" * 60)
print(" OOP Task 3: Access Specifiers & Encapsulation")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

class NeuralNetworkConfig:
    def __init__(self, architecture_name: str, learning_rate: float, secret_api_key: str):
        self.architecture_name = architecture_name  # Public member
        self._learning_rate = learning_rate          # Protected member (convention)
        self.__secret_api_key = secret_api_key      # Private member (Name mangling)

    # Property getter for protected member
    @property
    def learning_rate(self) -> float:
        return self._learning_rate

    # Property setter with validation
    @learning_rate.setter
    def learning_rate(self, value: float):
        if value <= 0 or value > 1.0:
            raise ValueError("Learning rate must be between 0 and 1.0")
        self._learning_rate = value

    # Method to reveal private member safely
    def authenticate_service(self, key_attempt: str) -> bool:
        return self.__secret_api_key == key_attempt

config = NeuralNetworkConfig("ResNet-50", 0.001, "KEY-9988-XYZ")

print("\n1. Accessing Public Member:")
print("   Architecture:", config.architecture_name)

print("\n2. Accessing Protected Member via Property:")
print("   Current Learning Rate:", config.learning_rate)
config.learning_rate = 0.005
print("   Updated Learning Rate:", config.learning_rate)

print("\n3. Testing Private Member Encapsulation:")
try:
    print(config.__secret_api_key)
except AttributeError as e:
    print("   [Encapsulation Success] Cannot directly access '__secret_api_key':", e)

print("\n4. Accessing Private Member via Name Mangling:")
# Python alters private attribute names to _ClassName__attrName
print("   Name Mangled value:", config._NeuralNetworkConfig__secret_api_key)

print("\n5. Testing Authentication Method:")
print("   Matches correct key?", config.authenticate_service("KEY-9988-XYZ"))
print("   Matches wrong key?  ?", config.authenticate_service("WRONG-KEY"))
