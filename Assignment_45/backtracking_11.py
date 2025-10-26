#Two natural numbers m and n are given.
#Display in all possible modalities the numbers from 1 to n, such that between any two numbers on consecutive positions,
#the difference in absolute value is at least m. If there is no solution, display a message.

def backtracking(n, m):
    if n < m:
        print("No valid sequence exists.")
        return
    seq = []
    used = [False] * (n+1)
    found = [False]
    def generate():
        if len(seq) == n:
            print(seq)
            found[0] = True
            return
        for i in range(1, n+1):
            if not used[i] and (not seq or abs(seq[-1] - i) >= m):
                seq.append(i)
                used[i] = True
                generate()
                seq.pop()
                used[i] = False
    generate()
    if not found[0]:
        print("No valid sequence exists.")

def main():
    n = int(input("Enter the maximum number in the list: "))
    m = int(input("Enter the minimum difference between two consecutive numbers: "))
    print("\nThese are the valid lists:")
    backtracking(n, m)

if __name__ == "__main__":
    main()