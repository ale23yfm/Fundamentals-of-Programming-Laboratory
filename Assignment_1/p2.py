# Solve the problem from the second set here
#Exercise 9
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int (n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def proper_factors(n):
    if is_prime(n):
        p = 0
    else:
        p = 1
        for d in range (2, n-1):
            if n % d == 0:
               p = p * d
    return p

def main():
    n = int(input("Type a number to find the product of its proper factors: "))
    p = proper_factors(n)

    if p == 0:
        print ("Number", n, "does not have proper factors.")
    else:
        print (p)

if __name__ == "__main__":
    main()