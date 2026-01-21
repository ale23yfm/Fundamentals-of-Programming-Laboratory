#brute force
def perm3():
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                pos_sol = [i,j,k]
                if i != j and j != k and i != k:
                    print(pos_sol)

#backtracking

if __name__  == "__main__":
    perm3()