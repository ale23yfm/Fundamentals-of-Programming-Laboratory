def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2
    left_side = array[:mid]
    right_side = array[mid:]
    merge_sort(left_side)
    merge_sort(right_side)
    merge(left_side,right_side, array)

def merge(l1,l2,lrez):
    i = j = 0
    l = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1
    while i < len(l1):
        l.append(l1[i])
        i += 1
    while j < len(l2):
        l.append(l2[j])
        j += 1
    lrez.clear()
    lrez.extend(l)


if __name__ == "__main__":
    array = [70, 20, 30, 90, 45, 50, 60, 10, 35]
    merge_sort(array)
    print(array)