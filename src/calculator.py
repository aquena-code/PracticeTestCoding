class Calculator:
    def add(self, valor1, valor2):
        return valor1 + valor2

    def valid_age(self, value):
        return 1 < value < 100

    def max_number(self, valor1, valor2, valor3):
        max_number = self.maximun(valor1, valor2)
        max_number = self.maximun(max_number, valor3)
        return max_number

    def maximun(self, valor1, valor2):
        if (valor1 >= valor2):
            return valor1
        else:
            return valor2