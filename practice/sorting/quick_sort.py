def partition(array, l, r):
    pivot = array[r]
    i = l - 1

    for j in range(l, r):
        if array[j] <= pivot:
            i += 1
            aux = array[i]
            array[i] = array[j]
            array[j] = aux
    aux = array[i+1]
    array[i+1] = array[r]
    array[r] = aux

    return i+1

def quick_sort(array, l, r):
    if l < r:
        p = partition(array, l, r)
        quick_sort(array, l, p-1)
        quick_sort(array, p+1, r)

if __name__ == "__main__":
    array = [70, 20, 30, 90, 45, 50, 60, 10, 35]
    quick_sort(array, 0, len(array)-1)
    print(array)