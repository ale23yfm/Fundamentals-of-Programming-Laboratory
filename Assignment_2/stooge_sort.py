def stooge_sort(arr, f, l):
#step 1: compare first and last element. If the first one is bigger, swap them.
    if arr[f] > arr[l]:
        c = arr[f]
        arr[f] = arr[l]
        arr[l] = c
    #step 2: calculate 1/3 of elements in the array
    p = int((l - f + 1) / 3)
    if l - f + 1 > 2:
        #step 3: sort first 2/3 of elements
        stooge_sort(arr, f, l - p)
        # step 4: sort last 2/3 of elements
        stooge_sort(arr, f + p, l)
        # step 5: sort again the first 2/3 of elements to ensure it is sorted correctly
        stooge_sort(arr, f, l - p)

def main():
    arr = list(map(int, input("Write the elements separated by space: ").split()))
    l = len(arr) - 1
    f = 0
    stooge_sort(arr, f, l)
    print("This is the sorted array by stooge sort method:")
    for i in range(0, len(arr)):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()