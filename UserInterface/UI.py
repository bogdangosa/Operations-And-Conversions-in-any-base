import Constants.constants
from Constants import constants
from Domains.Number import Number


class UI:

    def __init__(self):
        self.create_menu()

    @staticmethod
    def print_list_of_commands():
        print("Made by Bogdan Gosa")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Convert a number from it's base to any base ")
        print("0. Exit program ")

    @staticmethod
    def print_methods_menu():
        print("Choose one of those conversion methods:")
        print("1. Rapid conversion method")
        print("2. Substitution method")
        print("2. Successive division method")

    @staticmethod
    def read_complex_number():
        print("Set the base:",end=' ')
        base = int(input())
        print("Set the number:",end=' ')
        number = input()
        return Number(base,number)

    def create_menu(self):
        self.print_list_of_commands()
        command = int(input())
        while self.handle_command(command):
            self.print_list_of_commands()
            command = int(input())

    def add_two_numbers(self):
        number1 = self.read_complex_number()
        number2 = self.read_complex_number()
        print(number1+number2)

    def subtract_two_numbers(self):
        number1 = self.read_complex_number()
        number2 = self.read_complex_number()
        print(number1-number2)

    def multiply_number_with_digit(self):
        number1 = self.read_complex_number()
        print("Set the digit:",end=' ')
        digit = input()
        number2 = Number(number1.base,digit)
        print(number1*number2)

    def divide_number_with_digit(self):
        number1 = self.read_complex_number()
        print("Set the digit:",end=' ')
        digit = input()
        number2 = Number(number1.base,digit)
        print(number1//number2)

    def change_base(self):
        number = self.read_complex_number()
        print("The new base will be:",end=' ')
        base = int(input())
        best_method = number.get_recommended_method_for_conversion(base)
        self.print_methods_menu()
        selected_method = int(input())
        if selected_method != best_method:
            print("This is not the best method for this conversion")
            return
        number.base = base  # this changes the base and converts the number using the best method
        print(number)

    def handle_command(self,command):
        try:
            if command == constants.EXIT_COMMAND:
                return False
            elif command == constants.ADD_NUMBERS_COMMAND:
                self.add_two_numbers()
            elif command == constants.SUBTRACT_NUMBERS_COMMAND:
                self.subtract_two_numbers()
            elif command == constants.MULTIPLY_NUMBERS_COMMAND:
                self.multiply_number_with_digit()
            elif command == constants.DIVIDE_NUMBERS_COMMAND:
                self.divide_number_with_digit()
            elif command == constants.CHANGE_BASE_COMMAND:
                self.change_base()
        except ValueError as error:
            print(error)
        return True


if __name__ == '__main__':
    ui = UI()


