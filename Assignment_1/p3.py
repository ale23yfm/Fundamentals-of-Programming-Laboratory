# Solve the problem from the third set here
#Exercise 13
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sequence(x):
    index = 1
    result =  1
    cnt = x
    while cnt > 0:
        if index == 1 or is_prime(index):
            result = index
            cnt = cnt - 1
            index = index + 1
        else:
            for d in range(2, index - 1):
                if cnt > 0:
                    if is_prime(d):
                        if index % d == 0:
                            result = d
                            cnt = cnt - 1
            index = index + 1
    return result

def main():
    n = int(input("Type a number to determine the n-th element of the sequence of prime divisors of numbers: "))
    result = sequence(n)
    print("The n-th element of the sequence is", result)

if __name__ == "__main__":
    main()

    #1,2,3,2,5,2,3,7,2,3,2,5,11,2,3,13,2,7,3,5,2