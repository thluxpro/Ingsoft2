class FactorialCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FactorialCalculator, cls).__new__(cls)
        return cls._instance

    def factorial(self, n):
        if n < 0:
            raise ValueError("El número debe ser no negativo")
        return 1 if n == 0 else n * self.factorial(n - 1)

# Uso
calc = FactorialCalculator()
print(calc.factorial(10))  # Output: 120
