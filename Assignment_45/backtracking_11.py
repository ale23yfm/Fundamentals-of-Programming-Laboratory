#Two natural numbers m and n are given.
#Display in all possible modalities the numbers from 1 to n, such that between any two numbers on consecutive positions,
#the difference in absolute value is at least m. If there is no solution, display a message.

def menu():
    while True:
        print("\nChoose an option from the following list: ")
        print(" 1. Iterative Backtracking \n 2. Recursive Backtracking \n 3. Exit \n")
        try:
            o=int(input("Type your option: "))
        except ValueError:
            print("Invalid input. You must choose one of the options 1-3.")
            continue
        if o == 1:
            n = int(input("Enter the maximum number in the list: "))
            m = int(input("Enter the minimum difference between two consecutive numbers: "))
            if n < m:
                print("No valid sequence exists.")
                return
            else:
                print("\nThese are the valid lists:")
                backtracking_iter(n, m)
        elif o == 2:
            n = int(input("Enter the maximum number in the list: "))
            m = int(input("Enter the minimum difference between two consecutive numbers: "))
            if n < m:
                print("No valid sequence exists.")
                return
            else:
                print("\nThese are the valid lists:")
                backtracking_rec(n, m)
        elif o == 3:
            print("Thanks for playing!")
            exit()
        else:
            print("You must choose one of the options 1-3.")

def backtracking_rec(n, m, seq=None, used=None, found=False):
    # for i= 1->n we have:
    # 1->n, 2-> n-1, ..., n->1 choices which means O(n*(n-1)*...*2*1) = O(n!)
    if seq is None:
        seq = []
        used = [False] * (n+1)
        found = [False]
    if len(seq) == n:
        print(seq)
        return True
    for i in range(1, n+1):
        if not used[i] and (not seq or abs(seq[-1] - i) >= m):
            used[i] = True
            if backtracking_rec(n, m, seq + [i], used, found=True):
                found = True
            used[i] = False
    if seq == [] and not found:
        print("No valid sequence exists.")
    return found

def backtracking_iter(n, m):
    # for i= 1->n we have:
    # 1->n, 2-> n-1, ..., n->1 choices which means O(n*(n-1)*...*2*1) = O(n!)
    # abs(seq[i] - seq[i-1]) < m) this can improve the complexity, but in worst case it is O(n!)
    seq = [0] * (n + 1)
    used = [0] * (n + 1)
    i = 1
    found = False

    while i > 0:
        seq[i] += 1
        # find a valid number
        while seq[i] <= n and (used[seq[i]] or (i > 1 and abs(seq[i] - seq[i-1]) < m)):
            seq[i] += 1

        if seq[i] <= n:  # valid number
            used[seq[i]] = 1
            if i == n:
                print(seq[1:])
                found = True
                used[seq[i]] = 0  # find another one
            else:
                i += 1
                seq[i] = 0  # reset next position
        else:  # backtracking
            seq[i] = 0
            i -= 1
            if i > 0:
                used[seq[i]] = 0
    if not found:
        print("No valid sequence exists.")

def main():
    menu()

if __name__ == "__main__":
    main()