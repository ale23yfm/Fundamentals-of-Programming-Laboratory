#
# Write the implementation in this file
#

#A3. Determine the length and the elements of a longest subarray of numbers having increasing modulus.
#B1. Determine the length and the elements of a longest increasing subsequence, when considering each number's modulus.

def modulus(z):
    return (get_real(z) ** 2 + get_img(z) ** 2) ** 0.5

# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

#"""
def get_real(re):
    return re[0]

def get_img(im):
    return im[1]

def set_real(re, x):
    re[0] = x

def set_img(im, x):
    im[1] = x

def create_number(re, im):
    return [re, im]

def nr_to_str(z):
    re, im = z[0], z[1]
    if im == 0:
        return f"{re}"
    elif re == 0:
        return f"{im}i"
    elif im > 0:
        return f"{re}+{im}i"
    else:  # im < 0
        return f"{re}-{abs(im)}i"

#"""

#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

"""
def get_real(z):
    return z["real"]

def get_img(z):
    return z["img"]

def set_real(z, x):
    z["real"] = x

def set_img(z, x):
    z["img"] = x

def create_number(re, im):
    return {"real": re, "img": im}
    
def nr_to_str(z):
    re, im = z["real"], z["img"]
    if im == 0:
        return f"{re}"
    elif re == 0:
        return f"{im}i"
    elif im > 0:
        return f"{re}+{im}i"
    else:  # im < 0
        return f"{re}-{abs(im)}i"

"""

#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

#A3
def longest_increasing_subarray(numbers):
    max_len = 1
    max_start = 0
    start = 0
    for i in range(1, len(numbers)):
        if modulus(numbers[i]) > modulus(numbers[i-1]):
            if i - start + 1 > max_len:
                max_len = i - start + 1
                max_start = start
        else:
            start = i

    return max_len, numbers[max_start:max_start + max_len]

#B1
def longest_increasing_subsequence(numbers):
    n = len(numbers)
    dp = [1]*n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if modulus(numbers[j]) < modulus(numbers[i]) and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    index = dp.index(max_len)

    lis=[]
    while index != -1:
        lis.append(numbers[index])
        index = prev[index]

    lis.reverse()

    return max_len, lis

#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def read_number(numbers):
    while True:
        try:
            n = int(input("How many complex numbers do you want? Your answer is: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid choice. Please type a positive integer.")

    print("Enter your numbers as a+bi: ")
    for i in range(n):
        while True:
            z = input(f"{i+1}: ").replace(" ", "")

            if not all(ch.isdigit() or ch in "+-i" for ch in z):
                print("Invalid characters detected! Only digits, +, -, and i are allowed. Try again.")
                continue

            try:
                if z == "+i":
                    re = 0
                    im = 1
                elif z == "-i":
                    re = 0
                    im = -1

                # a+bi || a+i
                if "+" in z:
                    re, img = z.split("+")
                    re = int(re)

                    if img == "i" or img == "+i":
                        im = 1
                    elif img == "-i":
                        im = -1
                    else:
                        im = int(img.replace("i", ""))

                # a-bi || a-i
                elif "-" in z[1:]:
                    idx = z[1:].index("-") + 1
                    re = int(z[:idx])
                    im_part = z[idx:].replace("i", "")
                    if im_part == "" or im_part == "+":
                        im = 1
                    elif im_part == "-":
                        im = -1
                    else:
                        im = int(im_part)

                # bi
                elif "i" in z:
                    im = z.replace("i", "")
                    if im == "" or im == "+":
                        im = 1
                    elif im == "-":
                        im = -1
                    else:
                        im = int(im)
                    re = 0

                # a
                else:
                    re = int(z)
                    im = 0

                numbers.append(create_number(re, im))
                break
            except ValueError:
                print("Invalid number format! Please enter again.")

    return numbers

def print_number(numbers):
    print(numbers, "\n")
    print("   |   ".join(nr_to_str(z) for z in numbers))

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
            print("Do you and the default 10 complex numbers?")
            print(" 1. Yes. \n 2. No. \n 3. Go back. \n")
            try:
                w = int(input("Type your option: "))
            except ValueError:
                print("Invalid input. You must choose one of the options 1-3.")
                continue
            if w == 1:
                numbers.clear()
                print("There are the default numbers:")
                numbers = [create_number(3, 7), create_number(3, 4), create_number(1, -1), create_number(2,2), create_number(4, 0), create_number(-4, 2), create_number(0, 5), create_number(1, 2), create_number(3, 8)]
                print("Those are the numbers:")
                print_number(numbers)
            elif w == 2:
                numbers.clear()
                read_number(numbers)
                print_number(numbers)
            elif w == 3:
                continue
            else:
                print("Invalid choice. Please select 1-3.")
        elif o == 2:
            print_number(numbers)
        elif o == 3:
            print("Which problem do you want to see?")
            print(" 1. A. \n 2. B. \n 3. Go back. \n")
            w = int(input("Type your option: "))
            if w == 1:
                print("This is the subarray of numbers:")
                length, subarray = longest_increasing_subarray(numbers)
                print("Max length:", length)
                print("Subarray:", subarray)
                print_number(subarray)
            elif w == 2:
                print("This is the longest subsequence:")
                length, sequence = longest_increasing_subsequence(numbers)
                print("Max length:", length)
                print("Subsequence:", sequence)
                print_number(sequence)
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
    numbers = [create_number(3, 7), create_number(3, 4), create_number(1, -1), create_number(2, 2), create_number(4, 0),
               create_number(-4, 2), create_number(0, 5), create_number(1, 2), create_number(3, 8)]
    o = 0
    menu(o, numbers)

if __name__ == "__main__":
    main()