def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if array[j] < array[min_index]:
                min_index = j
        aux = array[i]
        array[i] = array[min_index]
        array[min_index] = aux

if __name__ == "__main__":
    array = [70, 20, 30, 90, 45, 50, 60, 10, 35]
    selection_sort(array)
    print(array)