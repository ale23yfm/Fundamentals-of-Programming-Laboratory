# Solve the problem from the first set here
#Exercise 5
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int (n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def largest_prime_number_below(n):
    for i in range (n-1, 1, -1):
        if is_prime(i):
            return i
    return None

def main():
    n = int(input("Type a number to provide the largest prime number smaller than it: "))
    result = largest_prime_number_below(n)
    if result is None:
        print ("A prime number smaller than", n, "does not exist.")
    else:
        print("The largest prime number smaller than", n, "is", result)

if __name__ == "__main__":
    main()