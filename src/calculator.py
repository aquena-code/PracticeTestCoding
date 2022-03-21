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

# For Exercise 4
    def is_vocal(self, valor):

        if(self.is_a_consonante(valor)):
            return "consonante"
        elif(self.is_a_vocal(valor)):
            return "vocal"
        elif(valor.isnumeric()):
            return "number"
        else:
            return "ninguno"

    def is_a_vocal(self, valor):
        vocales = ['a', 'e', 'i', 'o', 'u']

        try:
            vocales.index(valor.lower())
            return True
        except:
            return False

    def is_a_consonante(self, valor):
        consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

        try:
            consonantes.index(valor.lower())
            return True
        except:
            return False

#For exercise 5

    def reverse(self, cadena):
        reverse_chain = ""
        for character in cadena:
            reverse_chain = character + reverse_chain
        return reverse_chain

