class Calculadora:
    def soma(self, num1: int, num2: int) -> int:
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError("Ambos os valores devem ser inteiros.")
        return num1 + num2


num1 = int(input())
num2 = int(input())

calc = Calculadora()
print(calc.soma(num1, num2))