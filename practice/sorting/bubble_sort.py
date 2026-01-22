def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                aux = array[j+1]
                array[j+1] = array[j]
                array[j] = aux
                swapped = True
        if swapped == False:
            break

if __name__ == "__main__":
    array = [70, 20, 30, 90, 45, 50, 60, 10, 35]
    bubble_sort(array)
    print(array)