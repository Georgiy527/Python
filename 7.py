class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        #(a + bi)(c + di) = (ac - bd) + (ad + bc)i
        new_real = self.real*other.real - self.imaginary*other.imaginary
        new_imaginary = self.real*other.imaginary + self.imaginary*other.real
        return ComplexNumber(new_real, new_imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# Пример использования
complex_num1 = ComplexNumber(1, 2)
complex_num2 = ComplexNumber(3, 4)

print(complex_num1 + complex_num2) # Выведет: 4 + 6i
print(complex_num1 * complex_num2) # Выведет: -5 + 10i
