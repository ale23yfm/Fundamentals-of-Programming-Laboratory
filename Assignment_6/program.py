#
# Write the implementation in this file
#

#A3. Determine the length and the elements of a longest subarray of numbers having increasing modulus.
#B1. Determine the length and the elements of a longest increasing subsequence, when considering each number's modulus.

import random

# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

#Generates the random list with 10 complex numbers
def random_list(n):
    complex_list = []
    for i in range(n):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        complex_list.append(complex(a, b))
    return complex_list

#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

#Generates the random dict with 10 complex numbers
def random_dict(n):
    complex_dict = {}
    for i in range(n):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        complex_dict[i] = {"real": a, "img": b}
    return complex_dict

#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

#A3 with list
def longest_increasing_subarray_list(numbers):
    max_len = 1
    max_start = 0
    start = 0
    for i in range(1, len(numbers)):
        if abs(numbers[i]) > abs(numbers[i-1]):
            if i - start + 1 > max_len:
                max_len = i - start + 1
                max_start = start
        else:
            start = i

    return max_len, numbers[max_start:max_start + max_len]

#A3 with dict
def longest_increasing_subarray_dict(numbers):
    max_len = 1
    max_start = 0
    start = 0

    keys = list(numbers.keys())
    values = [numbers[k] for k in keys]

    for i in range(1, len(values)):
        mod_i = (values[i]["real"] ** 2 + values[i]["img"] ** 2) ** 0.5
        mod_prev = (values[i - 1]["real"] ** 2 + values[i - 1]["img"] ** 2) ** 0.5
        if mod_i > mod_prev:
            if i - start + 1 > max_len:
                max_len = i - start + 1
                max_start = start
        else:
            start = i

    longest_subdict = {}
    for i in range(max_len):
        longest_subdict[max_start + i] = numbers[max_start + i]

    return max_len, longest_subdict

#B1 with list
def longest_increasing_subsequence_list(numbers):
    n = len(numbers)
    mod = [abs(z) for z in numbers]
    subs = [[z] for z in numbers]

    for i in range(1, n):
        for j in range(i):
            if mod[i] > mod[j] and len(subs[j]) + 1 > len(subs[i]):
                subs[i] = subs[j] + [numbers[i]]

    longest_seq = max(subs, key=len)
    return len(longest_seq), longest_seq

#B1 with dict
def longest_increasing_subsequence_dict(numbers):
    if not numbers:
        return 0, {}

    keys = list(numbers.keys())
    values = [numbers[k] for k in keys]
    n = len(values)

    # Compute modulus
    mod = [(v["real"]**2 + v["img"]**2)**0.5 for v in values]

    # Initialize subsequences
    subs = [[v] for v in values]

    for i in range(1, n):
        for j in range(i):
            if mod[i] > mod[j] and len(subs[j]) + 1 > len(subs[i]):
                subs[i] = subs[j] + [values[i]]

    # Find the longest
    longest_seq = max(subs, key=len)

    # Convert back to dict with original keys
    # We take keys from values in order of longest_seq
    longest_dict = {}
    for idx, v in enumerate(longest_seq):
        # Find the original key corresponding to this value
        for k in keys:
            if numbers[k] == v and k not in longest_dict:
                longest_dict[k] = v
                break

    return len(longest_seq), longest_dict

#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

#Get the number for real/img part of complex numbers
def config_number(n):
    while True:
        try:
            n = int(input("Type the real part of the complex number: "))
            break
        except ValueError:
            print("Please enter a valid integer for the real part.")
    return n

#Places the real/img part in the list
def list_complex_numbers():
    n = int(input("How many complex numbers do you want? Your answer is: "))
    numbers = []
    for i in range(n):
        a = config_number("Type the real part of the complex number: ")
        b = config_number("Type the imaginary part of the complex number: ")
        z = complex(a, b)
        numbers.append(z)
    return numbers

#Places the real/img part in the dict
def dict_complex_numbers():
    n = int(input("How many complex numbers do you want? Your answer is: "))
    numbers = {}
    for i in range(n):
        a = config_number("Type the real part of the complex number: ")
        b = config_number("Type the imaginary part of the complex number: ")
        numbers[i] = {"real": a, "img": b}
    return numbers

#Shows the list
def display_list(numbers):
    if not numbers:
        print("No list of complex numbers yet. Please create one first. Choose option 1.")
    else:
        print("\nThis is your list of complex numbers:")
        print(numbers)
    return numbers

#Shows the dict
def display_dict(numbers):
    if not numbers:
        print("No dict of complex numbers yet. Please create one first. Choose option 1.")
    else:
        print("\nThis is your dict of complex numbers:")
        print(numbers)
    return numbers

#The following two help the menu to adapt to the list/dict mode
def text_list():
    print("list", end=" ")

def text_dict():
    print("dict", end=" ")


def print_a3_list(numbers):
    length, subarray = longest_increasing_subarray_list(numbers)
    print("Max length:", length)
    print("Subarray:", subarray)

def print_a3_dict(numbers):
    length, subarray = longest_increasing_subarray_dict(numbers)
    print("Max length:", length)
    print("Subarray:", subarray)


def print_b1_list(numbers):
    length, sequence = longest_increasing_subsequence_list(numbers)
    print("Max length:", length)
    print("Subsequence:", sequence)

def print_b1_dict(numbers):
    length, sequence = longest_increasing_subsequence_list(numbers)
    print("Max length:", length)
    print("Subsequence:", sequence)

def menu(o, numbers):
    while True:
        print("\nChoose an option from the following list: ")
        print(" 1. Read the numbers. \n 2. Display the numbers. \n 3. Display the subarray/subsequence. \n 4. Exit. \n")
        try:
            o=int(input("Type your option: "))
        except ValueError:
            print("Invalid choice. Please select 1-4.")
            continue
        if o == 1:
            print("Do you and the default", end=" ")
            # text_list()
            text_dict()
            print("with 10 complex numbers?")
            print(" 1. Yes. \n 2. No. \n 3. Go back. \n")
            try:
                w = int(input("Type your option: "))
            except ValueError:
                print("Invalid input. You must choose one of the options 1-3.")
                continue
            if w == 1:
                print("This is your default", end=" ")
                # text_list()
                text_dict()
                print("of complex numbers:")
                # numbers = random_list(10)
                numbers = random_dict(10)
                print (numbers)
            elif w == 2:
                # numbers = list_complex_numbers()
                numbers = dict_complex_numbers()
            elif w == 3:
                continue
            else:
                print("Invalid choice. Please select 1-3.")
        elif o == 2:
            # display_list(numbers)
            display_dict(numbers)
        elif o == 3:
            if not numbers:
                print("No", end=" ")
                # text_list()
                text_dict()
                print("of complex numbers yet. Please create one first. Choose option 1.")
            else:
                print("Which problem do you want to see?")
                print(" 1. A. \n 2. B. \n 3. Go back. \n")
                w = int(input("Type your option: "))
                if w == 1:
                    print("This is the subarray of numbers:")
                    # print_a3_list(numbers)
                    print_a3_dict(numbers)
                elif w == 2:
                    print("This is the longest subsequence:")
                    # print_b1_list(numbers)
                    print_b1_dict(numbers)
                elif w == 3:
                    continue
                else:
                    print("Invalid choice. Please select 1-3.")
        elif o == 4:
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice. Please select 1-4.")

def main():
    numbers = []
    o = 0
    menu(o, numbers)

if __name__ == "__main__":
    main()