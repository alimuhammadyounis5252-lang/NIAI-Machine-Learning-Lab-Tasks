# Week 2 - Task 27: User-Defined Exception Handling in Python
# Student Name: Ali Muhammad Younis (886)
# Reference: https://www.programiz.com/python-programming/user-defined-exception

print("=" * 60)
print(" Week 2 - Task 27: User-Defined Exception Handling")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# Base Application Error
class AIModelError(Exception):
    """Base exception for AI model errors."""
    pass

# Custom Exception for Invalid Input Range
class InvalidInputRangeError(AIModelError):
    def __init__(self, value, min_val, max_val):
        super().__init__(f"Value {value} is out of permitted range [{min_val}, {max_val}].")
        self.value = value
        self.min_val = min_val
        self.max_val = max_val

# Custom Exception for Model Not Trained
class ModelNotFittedError(AIModelError):
    def __init__(self, model_name):
        super().__init__(f"The model '{model_name}' has not been trained yet. Call .fit() first.")
        self.model_name = model_name

# Demonstration class using custom exceptions
class ProbabilityPredictor:
    def __init__(self):
        self.is_trained = False

    def train(self):
        self.is_trained = True
        print("Model successfully trained.")

    def predict_probability(self, confidence_score: float):
        if not self.is_trained:
            raise ModelNotFittedError("ProbabilityPredictor")
        if not (0.0 <= confidence_score <= 1.0):
            raise InvalidInputRangeError(confidence_score, 0.0, 1.0)
        return f"Predicted probability: {confidence_score * 100:.2f}%"

# Testing Custom Exceptions
predictor = ProbabilityPredictor()

# Test 1: Predict before training -> raises ModelNotFittedError
try:
    predictor.predict_probability(0.85)
except ModelNotFittedError as e:
    print(f"[TEST 1 CAUGHT] {e}")

# Train the model
predictor.train()

# Test 2: Invalid input range -> raises InvalidInputRangeError
try:
    predictor.predict_probability(1.75)
except InvalidInputRangeError as e:
    print(f"[TEST 2 CAUGHT] {e} (value={e.value})")

# Test 3: Valid execution
result = predictor.predict_probability(0.92)
print(f"[TEST 3 SUCCESS] {result}")
