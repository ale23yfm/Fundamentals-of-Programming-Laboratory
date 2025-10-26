def backtracking(n, m):
    if n < m:
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
            if not used[i] and (not seq or abs(seq[-1] - i)):
                seq.append(i)
                used[i] = True
                generate()


def main():
    n = int(input("Enter the maximum number in the list: "))
    m = int(input("Enter the minimum difference between two consecutive numbers: "))
    print("These are the valid lists:")
    backtracking(n, m)

if __name__ == "__main__":
    main()