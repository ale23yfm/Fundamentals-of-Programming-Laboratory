def binary_search(array, x):
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = (r + l) // 2

        if array[mid] == x:
            return mid

        if array[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

if __name__ == "__main__":
    array = [70, 20, 30, 90, 45, 50, 60, 10, 35]
    print (binary_search(array, 30))