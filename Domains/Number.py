import copy
import math

from Constants import constants

STRING_TO_NUMBERS_ARRAY = \
    {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16}
RAPID_CONVERSION_TABLE = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111",
}


class Number:

    def __init__(self,base: int,number: str):
        self.__base = base
        self.__number = number

    @property
    def base(self):
        return self.__base

    @property
    def number(self):
        return self.__number

    @base.setter
    def base(self, new_base):
        if Number.is_power_of_two(self.base) and Number.is_power_of_two(new_base):
            self.__number = self.rapid_conversion_method(new_base)
        elif self.base < new_base:
            self.__number = self.substitution_method_conversion(new_base).number
        elif self.base > new_base:
            self.__number = self.successive_division_conversion(new_base)
        self.__base = new_base

    @number.setter
    def number(self, new_number):
        self.__number = new_number

    def get_recommended_method_for_conversion(self,new_base):
        """
        You send this function the base you want to convert to, and it tells you the best method for it
        :param new_base: the base for which you want to know what the best conversion method is
        :return: A constant: RAPID_CONVERSION_METHOD , SUBSTITUTION_METHOD or SUCCESSIVE_DIVISION_METHOD
        """
        if Number.is_power_of_two(self.base) and Number.is_power_of_two(new_base):
            return constants.RAPID_CONVERSION_METHOD
        if self.base < new_base:
            return constants.SUBSTITUTION_METHOD
        elif self.base > new_base:
            return constants.SUCCESSIVE_DIVISION_METHOD

    @staticmethod
    def string_digit_to_int(digit: str):
        """

        :param digit: a digit as a string with values between 0-F
        :return: the value of the digit in base 10, int
        """
        return STRING_TO_NUMBERS_ARRAY[digit]

    @staticmethod
    def int_value_to_digit(digit_value: int):
        """

        :param digit_value: the value of the digit in base 10, int
        :return: a digit as a string with values between 0-F
        """
        return list(STRING_TO_NUMBERS_ARRAY.keys())[list(STRING_TO_NUMBERS_ARRAY.values()).index(digit_value)]

    @staticmethod
    def digit_to_base_2(digit: str,original_base) -> str:
        """
        Converts the digit to base 2 using the rapid conversion table
        :param digit:
        :param original_base:
        :return:
        """
        result = RAPID_CONVERSION_TABLE[digit]
        if original_base == 16:
            return result
        elif original_base == 8:
            return result[1:]
        elif original_base == 4:
            return result[2:]

    @staticmethod
    def base2_to_digit(digit_in_base_2):
        while len(digit_in_base_2) < 4:
            digit_in_base_2 = "0"+digit_in_base_2
        return list(RAPID_CONVERSION_TABLE.keys())[list(RAPID_CONVERSION_TABLE.values()).index(digit_in_base_2)]

    @staticmethod
    def reverse_string(string: str):
        return string[::-1]

    def __str__(self):
        return "Base: " + str(self.__base) + ", Number: " + self.__number

    def __eq__(self, other):
        if not isinstance(other,Number):
            return False
        return self.__number == other.number and self.__base == other.base

    @staticmethod
    def is_power_of_two(base):
        """
        Checks if the base is a power of two
        :param base:
        :return: True if the base is power of 2, False otherwise
        """
        while base % 2 == 0:
            base /= 2
        return base == 1

    @staticmethod
    def remove_zeros_at_the_start_of_string(string):
        """
        Removes every 0 from the beginning of a string
        :param string:
        :return: The string without the 0 from the beginning
        """
        while string[0] == "0":
            string = string[1:]
        return string

    def rapid_conversion_method(self,new_base):
        number_in_base_2 = self.rapid_conversion_to_base_2()
        if new_base != 2:
            number_in_base_2 = self.from_base_2_to_another_base_multiple_of_2(new_base, number_in_base_2)
        number_in_base_2 = Number.remove_zeros_at_the_start_of_string(number_in_base_2)
        return number_in_base_2

    def rapid_conversion_to_base_2(self):
        new_number = ""
        for digit in self.number:
            new_number = new_number + Number.digit_to_base_2(digit,self.__base)
        return new_number

    def from_base_2_to_another_base_multiple_of_2(self,new_base,number_in_base_2):
        number_in_base_2_reversed = self.reverse_string(number_in_base_2)
        digits_required = int(math.log(new_base,2))
        new_number = ""
        for index in range(0,len(number_in_base_2_reversed),digits_required):
            digit = Number.reverse_string(number_in_base_2_reversed[index:index+digits_required])
            new_number = Number.base2_to_digit(digit) + new_number
        return new_number

    def substitution_method_conversion(self,new_base):
        number_value = self.reverse_string(self.number)
        old_base_number = Number(new_base, Number.int_value_to_digit(self.base))
        multiplier = Number(new_base, "1")
        final_number = Number(new_base, "0")
        for index in range(0, len(number_value)):
            current_digit = Number(new_base, number_value[index])
            number_to_be_added = multiplier * current_digit
            final_number = final_number + number_to_be_added
            multiplier = multiplier * old_base_number
        return final_number

    @staticmethod
    def valid(number_value,new_base):
        if len(number_value) > 1:
            return True
        return Number.string_digit_to_int(number_value) >= new_base

    def successive_division_conversion(self,new_base):
        number_copy = copy.deepcopy(self)
        number_copy.number = "0" + number_copy.number
        number_value = "0" + self.__number
        old_base = self.__base
        final_number = ""
        while Number.valid(number_value,new_base):
            division_result,division_reminder = number_copy.__div_and_mod(Number(old_base,Number.int_value_to_digit(new_base)))
            number_copy.number = division_result
            final_number = division_reminder + final_number
            number_value = division_result
        final_number = number_value + final_number
        return final_number

    def __add__(self, other):
        """

        :param other:
        :return: the result of the addition
        """
        if self.base != other.base:
            raise ValueError("Not the same base")
        base = self.base
        # Putting the operands in these variables reversed, for convenience
        number1_value = Number.reverse_string(self.number)
        number2_value = Number.reverse_string(other.number)
        new_number = ""
        carry = 0
        last_index = 0
        for index in range(0,min(len(number1_value),len(number2_value))):
            # getting the digits in int base 10 form
            digit1 = Number.string_digit_to_int(number1_value[index])
            digit2 = Number.string_digit_to_int(number2_value[index])
            new_digit = digit1 + digit2 + carry  # adding the digits as well as the carry value
            if new_digit >= base:  # verify if the new digit is bigger than the base
                new_digit -= base  # if it is, set the carry to 1 and subtract the base
                carry = 1
            else:
                carry = 0  # if not, set the carry to 0
            new_number = Number.int_value_to_digit(new_digit) + new_number  # append the digit to the final number
            last_index = index

        if len(number2_value) > len(number1_value):  # put the number that still has digits in number1
            number1_value = number2_value
        for index in range(last_index+1,len(number1_value)):  # complete the result with the remaining digits of the bigger number
            digit = Number.string_digit_to_int(number1_value[index])
            new_digit = digit + carry
            if new_digit >= base:
                new_digit -= base
                carry = 1
            else:
                carry = 0
            new_number = Number.int_value_to_digit(new_digit) + new_number
        if carry == 1:  # if you still have a carry, append it in front
            new_number = str(carry) + new_number
        return Number(base,new_number)  # create the result Number object and return it

    def __sub__(self, other):
        if self.base != other.base:
            raise ValueError("Not the same base")
        base = self.base
        # Putting the operands in these variables reversed, for convenience
        number1_value = Number.reverse_string(self.number)
        number2_value = Number.reverse_string(other.number)
        new_number = ""
        carry = 0
        last_index = 0
        for index in range(0, min(len(number1_value), len(number2_value))):
            # getting the digits in int base 10 form
            digit1 = Number.string_digit_to_int(number1_value[index])
            digit2 = Number.string_digit_to_int(number2_value[index])
            new_digit = digit1 - digit2 - carry  # subtracting the digits as well as the carry value
            if new_digit < 0:  # if the new digit is less than zero we need to borrow a 1
                new_digit = base + new_digit  # adding the borrowed digit as the base to the new digit, and setting the carry to 1
                carry = 1
            else:
                carry = 0  # clearing the carry
            new_number = Number.int_value_to_digit(new_digit) + new_number  # append the digit to the final number
            last_index = index
        for index in range(last_index+1,len(number1_value)):
            if carry:
                digit = Number.string_digit_to_int(number1_value[index]) - carry
                if digit < 0:
                    digit = base + digit
                    carry = 1
                else:
                    carry = 0
                new_number = Number.int_value_to_digit(digit) + new_number
                continue
            new_number = number1_value[index] + new_number - carry
        new_number = Number.remove_zeros_at_the_start_of_string(new_number)
        return Number(base, new_number)

    def __mul__(self, other):
        if self.base != other.base:
            raise ValueError("Not the same base")
        if len(other.number) > 1:
            raise ValueError("Can't perform multiplication by more than one digit")
        # revert number for convenience
        number_value = Number.reverse_string(self.number)
        new_number = ""
        multiplier = Number.string_digit_to_int(other.number)  # convert string number to int
        base = self.base
        carry = 0
        for index in range(0, len(number_value)):
            digit = Number.string_digit_to_int(number_value[index])
            new_digit = digit * multiplier + carry
            if new_digit > base:
                carry = new_digit // base
                new_digit = new_digit % base
            else:
                carry = 0
            new_number = Number.int_value_to_digit(new_digit) + new_number
        if carry > 0:
            new_number = Number.int_value_to_digit(carry) + new_number
        return Number(base, new_number)

    def __div_and_mod(self, other):
        if self.base != other.base:
            raise ValueError("Not the same base")
        if len(other.number) > 1:
            raise ValueError("Can't perform division by more than one digit")
        number_value = self.number
        divider = Number.string_digit_to_int(other.number)
        final_number = ""
        tens_digit = "0"
        while len(number_value) >= 1:
            last_digit = number_value[0]
            value = Number.string_digit_to_int(tens_digit) * self.base + Number.string_digit_to_int(last_digit)
            tens_digit = Number.int_value_to_digit(value % divider)
            final_number += Number.int_value_to_digit(value // divider)
            number_value = number_value[1:]
        final_number = Number.remove_zeros_at_the_start_of_string(final_number)
        return final_number, tens_digit

    def __floordiv__(self, other):
        """

        :param other: divider
        :return: The result of the division with one digit
        """
        div_result = self.__div_and_mod(other)
        return Number(self.base,div_result[0])

    def __mod__(self, other):
        """

        :param other: divider
        :return: The remainder of the division with one digit
        """
        div_result = self.__div_and_mod(other)
        return Number(self.base,div_result[1])
