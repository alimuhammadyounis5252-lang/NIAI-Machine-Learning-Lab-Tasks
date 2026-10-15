# Week 2 - OOP Task 2: Inheritance & Method Resolution Order (MRO)
# Student Name: Ali Muhammad Younis (886)

print("=" * 60)
print(" OOP Task 2: Inheritance (Single, Multilevel, Hierarchical, Multiple)")
print(" Student: Ali Muhammad Younis (886)")
print("=" * 60)

# 1. Base Class
class Estimator:
    def __init__(self, name: str):
        self.name = name

    def fit(self, data):
        print(f"[{self.name}] Fitting parameters on dataset of size {len(data)}...")

    def evaluate(self):
        print(f"[{self.name}] Base evaluation completed.")

# 2. Single Inheritance
class SupervisedEstimator(Estimator):
    def __init__(self, name: str, target_column: str):
        super().__init__(name)
        self.target_column = target_column

    def describe(self):
        print(f"Supervised Model: {self.name}, Target: {self.target_column}")

# 3. Multilevel Inheritance
class LinearRegressor(SupervisedEstimator):
    def __init__(self, name: str = "Linear Regression"):
        super().__init__(name, target_column="Continuous Output")

    def fit(self, data):
        super().fit(data)
        print(f"[{self.name}] Computed optimal weights via Ordinary Least Squares.")

# 4. Hierarchical Inheritance (Another branch from SupervisedEstimator)
class LogisticClassifier(SupervisedEstimator):
    def __init__(self, name: str = "Logistic Regression"):
        super().__init__(name, target_column="Discrete Category")

    def fit(self, data):
        super().fit(data)
        print(f"[{self.name}] Optimized Log-Loss via Gradient Descent.")

# 5. Multiple Inheritance and Method Resolution Order (MRO)
class FeatureTransformer:
    def transform(self):
        return "Features scaled and normalized."

class PipelineModel(LinearRegressor, FeatureTransformer):
    def __init__(self, name: str = "Pipeline_LinReg"):
        super().__init__(name)

print("\n--- Demonstrating Multilevel & Hierarchical Inheritance ---")
reg = LinearRegressor()
reg.describe()
reg.fit([1, 2, 3, 4, 5])

clf = LogisticClassifier()
clf.describe()
clf.fit([0, 1, 0, 1, 1])

print("\n--- Demonstrating Multiple Inheritance & MRO ---")
pipe = PipelineModel()
print("Transformer Output:", pipe.transform())
print(f"MRO for PipelineModel:\n{[cls.__name__ for cls in PipelineModel.__mro__]}")
