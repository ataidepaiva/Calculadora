import sys

class Calculator:
    def __init__(self):
        self.current_value = 0
        self.fita = []

    def add(self, value):
        self.fita.append(f'{self.current_value} + {value} = {self.current_value + value}')
        self.current_value += value

    def subtract(self, value):
        self.fita.append(f'{self.current_value} - {value} = {self.current_value - value}')
        self.current_value -= value

    def multiply(self, value):
        self.fita.append(f'{self.current_value} * {value} = {self.current_value * value}')
        self.current_value *= value

    def divide(self, value):
        self.fita.append(f'{self.current_value} / {value} = {self.current_value / value}')
        self.current_value /= value

    def clear(self):
        self.current_value = 0
        self.fita = []

if __name__ == '__main__':
    calculator = Calculator()

    while True:
        command = input('Digite o comando (+, -, *, /, c, s, q): ')
        if command == '+':
            value = float(input('Digite o valor a ser adicionado: '))
            calculator.add(value)
            print(f'Resultado: {calculator.current_value}')
        elif command == '-':
            value = float(input('Digite o valor a ser subtraído: '))
            calculator.subtract(value)
            print(f'Resultado: {calculator.current_value}')
        elif command == '*':
            value = float(input('Digite o valor a ser multiplicado: '))
            calculator.multiply(value)
            print(f'Resultado: {calculator.current_value}')
        elif command == '/':
            value = float(input('Digite o valor a ser dividido: '))
            calculator.divide(value)
            print(f'Resultado: {calculator.current_value}')
        elif command == 'c':
            calculator.clear()
            print('Fita apagada')
        elif command == 's':
            print('Fita:')
            for linha in calculator.fita:
                print(linha)
        elif command == 'q':
            sys.exit()
