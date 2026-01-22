def insertion_sort(array):
    for i in range(1, len(array)):
        val = array[i]
        j = i-1
        while j >= 0 and array[j] > val:
            array[j+1] = array[j]
            j = j - 1
            array[j + 1] = val
        print (array)

if __name__ == "__main__":
    array = [70, 20, 30, 90, 45, 50, 60, 10, 35]
    print(array)
    insertion_sort(array)
    print(array)