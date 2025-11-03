#1. Determine the longest common subsequence of two given sequences.
# Subsequence elements are not required to occupy consecutive positions.
# For example, if `X = "MNPNQMN"` and `Y = "NQPMNM"`,
# the longest common subsequence has length `4`, and can be one of `"NQMN"`, `"NPMN"` or `"NPNM"`.
# Determine and display both the length of the longest common subsequence as well as at least one such subsequence.

def menu():
    while True:
        print("\nChoose an option from the following list: ")
        print(" 1. Naive Version \n 2. Dynamic Version \n 3. Exit \n")
        try:
            o=int(input("Type your option: "))
        except ValueError:
            print("Invalid input. You must choose one of the options 1-3.")
            continue
        if o == 1:
            n = input("Enter the first list: ")
            m = input("Enter the second list: ")
            length, seq = lcs_naive(n, m)
            print("The maximum length is:", length)
            print("This is a valid sequence:", seq)
        elif o == 2:
            n = input("Enter the first list: ")
            m = input("Enter the second list: ")
            length, seq = lcs_dynamic(n, m)
            print("The maximum length is:", length)
            print("This is a valid sequence:", seq)
        elif o == 3:
            print("Thanks for playing!")
            exit()
        else:
            print("You must choose one of the options 1-3.")

def lcs_dynamic(x, y):
    #O(m*n)
    #we calculate each cell
    m, n = len(x)+1, len(y)+1
    res = [[0 for _ in range(n)] for _ in range(m)] #completed first row and column with 0
    for i in range(1, m):
        for j in range(1, n):
            if x[i-1] == y[j-1]:
                res[i][j] = res[i-1][j-1] + 1
            else:
                res[i][j] = max(res[i][j-1], res[i-1][j])

    length = res[m-1][n-1]
    i, j = m-1, n-1
    subseq = []
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            subseq.append(x[i - 1])
            i -= 1
            j -= 1
        elif res[i - 1][j] > res[i][j - 1]:
            i -= 1
        else:
            j -= 1
    subseq.reverse()
    return length, ''.join(subseq)

def lcs_naive(x, y):
    #O(2^(m+n))
    #for each number are 2 options: keep it or ignore it
    #so 2^n * 2^m
    if not x or not y:
        return 0, ""
    if x[-1] == y[-1]:
        length, subseq = lcs_naive(x[:-1], y[:-1])
        return length + 1, subseq + x[-1]
    else:
        l1, s1 = lcs_naive(x[:-1], y)
        l2, s2 = lcs_naive(x, y[:-1])
        if l1 > l2:
            return l1, s1
        else:
            return l2, s2


def main():
    menu()

if __name__ == "__main__":
    main()