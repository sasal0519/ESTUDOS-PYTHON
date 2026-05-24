class ConversorTemperatura:
    """
    Classe responsável por converter temperaturas de Celsius para Fahrenheit.
    """

    def celsius_para_fahrenheit(self, celsius: float) -> float:
        """
        Converte uma temperatura em Celsius para Fahrenheit.
        
        Fórmula: F = (C × 9/5) + 32
        """
        return (celsius * 9 / 5) + 32


# Entrada do usuário
celsius = float(input())

# Criando uma instância do conversor
conversor = ConversorTemperatura()

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)