def no_digits(n):
    if n < 0:
        n = -n
    if n == 0:
        return 1
    cnt = 0
    while n>0:
        cnt += 1
        n //= 10
    return cnt

if __name__ == "__main__":
    print(no_digits(-14320))
