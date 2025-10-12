def interpolation_search(arr, f, l, n):
    #Now compare the first element with all the elements that come after it
    if f < l and n > arr[f] and f < arr[l]:
        pos = f +(l - f) // (arr[l] - arr[f]) * (n - arr[f])
        if arr[pos] == n:
            return pos
        elif arr[pos] < n:
            return interpolation_search(arr, pos + 1, l, n)
        else:
            return interpolation_search(arr, pos - 1, l, n)
    return -1

def main():
    arr = list(map(int, input("Write the elements separated by space: ").split()))
    x = int(input("Enter the index of the element to be found: "))

    index = interpolation_search(arr, 0, len(arr) - 1, x)

    if index == -1:
        print("Element not found")
    else:
        print("Element found at index: ", index)

if __name__ == "__main__":
    main()