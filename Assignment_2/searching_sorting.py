import random

from configobj.validate import is_integer

# --- MENU ---

def menu(a, was_sorted):
    while True:
        print("\nChoose an option from the following list: ")
        print(" 1. Generate a random list of numbers. \n 2. Search for an item in the list. \n 3. Sort the list using ascending exchange sort. \n 4. Sort the list using stooge sort. \n 5. Exit. \n")
        try:
            o=int(input("Type your option: "))
        except ValueError:
            print("Invalid input. You must choose one of the options 1-5.")
            continue
        if o == 1:
            a, was_sorted = option_1(a, was_sorted)
        elif o == 2:
            a, was_sorted = option_2(a, was_sorted)
        elif o == 3:
            a, was_sorted = option_3(a, was_sorted)
        elif o == 4:
            a, was_sorted = option_4(a, was_sorted)
        elif o == 5:
            print("Thanks for playing!")
            exit()
        else:
            print("You must choose one of the options 1-5.")

def option_1(a, was_sorted):
    while True:
        try:
            n = int(input("Type the number of elements in the list: "))
            if n < 1:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    a = random.sample(range(1, 1000), n)
    print("The elements in the list are: ", a, "\n")
    was_sorted = False
    return a, was_sorted

def option_2(a, was_sorted):
    if len(a) == 0:
        print("You must generate a list. Please choose option 1.")
        return a, was_sorted
    elif not was_sorted:
        print("You must sort the list. Please choose option 3, 4 or 5.")
        return a, was_sorted
    else:
        print("The elements in the list are: ", a, "\n")
        while True:
            try:
                n = int(input("Type the number you want to search in the list:"))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        index = interpolation_search(a, 0, len(a) - 1, n)
        if index == -1:
            print(n, "was not found in the list.\n")
        else:
            print(n, "is placed at the index: ", index, "\n")
        return a, was_sorted

def option_3(a, was_sorted):
    if len(a) == 0:
        print("You must generate a list. Please choose option 1.")
        return a, was_sorted
    elif was_sorted:
        print("Your list is sorted.")
        return a, was_sorted
    else:
        was_sorted = True
        while True:
            try:
                step = int(input("Type the number of steps to be displayed:"))
                if step < 1:
                    print("Step must be at least 1.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        exchange_sort_asc(a, step)
        print("The elements in the list are now: ", a, "\n")
        return a, was_sorted

def option_4(a, was_sorted):
    if len(a) == 0:
        print("You must generate a list. Please choose option 1.")
        return a, was_sorted
    elif was_sorted:
        print("Your list is sorted.")
        return a, was_sorted
    else:
        was_sorted = True
        count = [0]
        while True:
            try:
                step = int(input("Type the number of steps to be displayed: "))
                if step < 1:
                    print("Step must be at least 1.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        stooge_sort(a, 0, len(a) - 1, step, count)
        print("The elements in the list are now: ", a, "\n")
        return a, was_sorted

# --- Sorting Algorithms ---

def exchange_sort_asc(arr, step):
    l = len(arr)
    count = 0
    #Now compare the first element with all the elements that come after it
    for i in range (0, l - 1):
        for j in range (i + 1, l):
            if arr[i] > arr[j]:
                c = arr[j]
                arr[j] = arr[i]
                arr[i] = c
                count += 1
            if count % step == 0:
                print("Partial sorted list now:", arr, "\n")

def stooge_sort(arr, f, l, step, count):
#step 1: compare first and last element. If the first one is bigger, swap them.
    if arr[f] > arr[l]:
        c = arr[f]
        arr[f] = arr[l]
        arr[l] = c
    #step 2: calculate 1/3 of elements in the array
    p = int((l - f + 1) / 3)
    if l - f + 1 > 2:
        #step 3: sort first 2/3 of elements
        stooge_sort(arr, f, l - p, step, count)
        count[0] += 1
        if count[0] % step == 0:
            print("Partial sorted list now:", arr, "\n")
        # step 4: sort last 2/3 of elements
        stooge_sort(arr, f + p, l, step, count)
        count[0] += 1
        if count[0] % step == 0:
            print("Partial sorted list now:", arr, "\n")
        # step 5: sort again the first 2/3 of elements to ensure it is sorted correctly
        stooge_sort(arr, f, l - p, step, count)
        count[0] += 1
        if count[0] % step == 0:
            print("Partial sorted list now:", arr, "\n")

# --- Searching Algorithms ---

def interpolation_search(arr, f, l, n):
    if f <= l and arr[f] <= n <= arr[l]:
        if arr[f] == arr[l]:
            if arr[f] == n:
                return f
            else:
                return -1

        else:
            pos = f + ((l - f) * (n - arr[f])) // (arr[l] - arr[f])
            if arr[pos] == n:
                return pos
            elif arr[pos] < n:
                return interpolation_search(arr, pos + 1, l, n)
            else:
                return interpolation_search(arr, f, pos - 1, n)
    return -1

if __name__ == "__main__":
    a = []
    was_sorted = False
    print("Welcome to the MENU!")
    menu(a, was_sorted)