#Those algorithms do not show any steps during sorting

def exchange_sort_asc_alg(arr):
    l = len(arr)
    #Now compare the first element with all the elements that come after it
    for i in range (0, l - 1):
        for j in range (i + 1, l):
            if arr[i] > arr[j]:
                c = arr[j]
                arr[j] = arr[i]
                arr[i] = c

def stooge_sort_alg(arr, f, l):
#step 1: compare first and last element. If the first one is bigger, swap them.
    if arr[f] > arr[l]:
        c = arr[f]
        arr[f] = arr[l]
        arr[l] = c
    #step 2: calculate 1/3 of elements in the array
    p = int((l - f + 1) / 3)
    if l - f + 1 > 2:
        #step 3: sort first 2/3 of elements
        stooge_sort_alg(arr, f, l - p)
        # step 4: sort last 2/3 of elements
        stooge_sort_alg(arr, f + p, l)
        # step 5: sort again the first 2/3 of elements to ensure it is sorted correctly
        stooge_sort_alg(arr, f, l - p)