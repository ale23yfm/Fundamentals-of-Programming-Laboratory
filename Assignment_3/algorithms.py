#Those algorithms do not show any steps during sorting

def exchange_sort_asc_alg(arr):
    #The complexity of the algorithm is:
    # for i -> l-1 which is linear so it is O(n)
    # for j -> it depends on i so for each i we have a j
    # i->j : 0->n-1, 1->n-2, 2->n-3 ... n-4-> 3(n-3, n-2, n-1), n-3->2 (n-2, n-1), n-2->1(n-1)
    # Now we sum them: (n-1)+(n-2)+(n-3)+...+2+1 = (Gauss Summation) = (n-1)(n-2)/2 = (n^2-3n+2)/2
    # We consider the grates power so complexity is O(n^2)

    # Best case is when the list is sorted so it is linear: O(n)
    # Worst case is when the list is sorted descendent so we have to swap every two elements in pairs, so it is O(n^2)

    l = len(arr)
    #Now compare the first element with all the elements that come after it
    for i in range (0, l - 1):
        for j in range (i + 1, l):
            if arr[i] > arr[j]:
                c = arr[j]
                arr[j] = arr[i]
                arr[i] = c

def stooge_sort_alg(arr, f, l):
    # Recursion formula T(n): 3(2n/3) + c
    # 3 because the function is called 3 times recursively
    # 2n/3 because we treat the 2/3 part of the list
    # c for swapping elements

    # From Master Theorem: T(n): a(n/b) + c = O(n^log_b a)
    # In this case O(n^log_3/2 3) which is approximately O(n^2.70951)

    # Because it is a slow algorithm, best and worst cases work exactly the same time.

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