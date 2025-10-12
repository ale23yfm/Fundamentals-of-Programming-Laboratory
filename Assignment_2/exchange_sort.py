# Exchange sort method works on both ascending and descending

#There is the ascending way:
def exchange_sort_asc(arr):
    l = len(arr)
    #Now compare the first element with all the elements that come after it
    for i in range (0, l - 1):
        for j in range (i + 1, l):
            if arr[i] > arr[j]:
                c = arr[j]
                arr[j] = arr[i]
                arr[i] = c

#There is the descending way:
def exchange_sort_desc(arr):
    l = len(arr)
    #Now compare the first element with all the elements that come after it
    for i in range (0, l - 1):
        for j in range (i + 1, l):
            if arr[i] < arr[j]:
                c = arr[j]
                arr[j] = arr[i]
                arr[i] = c

def main():
    arr = list(map(int, input("Write the elements separated by space: ").split()))

    exchange_sort_asc(arr)
    print("This is the sorted array by ascending exchange sort method:")
    for i in range(0, len(arr)):
        print(arr[i], end=' ')

    exchange_sort_desc(arr)
    print("\nThis is the sorted array by descending exchange sort method:")
    for i in range(0, len(arr)):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()