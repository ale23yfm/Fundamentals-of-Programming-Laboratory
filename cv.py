import math

def alternating_sum_to_ln2(x):
    res = 0.0
    for i in range(1, x + 1):
        res += (-1) ** (i + 1) / i
    return res

def rearranged_sum(x):
    res = 0.0
    pos = 3
    count_pos = 1
    count_neg = 2
    neg = 4
    count = 0
    while count < x:
        for i in range(pos):
            if count < x:
                res += 1 / count_pos
                count_pos += 1
                count += 1
            else:
                break
        for i in range(neg):
            if count < x:
                res -= 1 / count_neg
                count_neg += 1
                count += 1
            else:
                break
    return res

if __name__ == "__main__":
    ln2 = math.log(2)
    n = 100000

    sum1 = alternating_sum_to_ln2(n)
    print("Alternating sum: ")
    print ("ln2 = ", ln2)
    print ("sum = ", sum1, '\n')

    sum2 = rearranged_sum(n)
    print("Rearranged sum: ")
    print("ln2 = ", ln2)
    print("sum = ", sum2)