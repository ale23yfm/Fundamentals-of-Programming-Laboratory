class Product:
    def __init__(self, name, type, price):
        self._name = name
        self._type = type
        self._price = price

    def __str__(self):
        return f"{self._name}, {self._type}, {self._price}"

class Product_service:
    def __init__(self):
        self._p = []

    def add(self, product):
        self._p.append(product)

    def get_all(self):
        return self._p

def merge_sort(array, key= lambda x: x, reverse = False):
    if (len(array) <= 1):
        return array
    mid = len(array)//2
    left_side = merge_sort(array[:mid], key, reverse)
    right_side = merge_sort(array[mid:], key, reverse)
    return merge(left_side, right_side, key, reverse)

def merge(l1,l2,key, reverse):
    i = 0
    j = 0
    l = []
    while i < len(l1) and j < len(l2):
        if not reverse:
            if key(l1[i]) < key(l2[j]):
                l.append(l1[i])
                i=i+1
            else:
                l.append(l2[j])
                j = j+1
        else:
            if key(l1[i]) > key(l2[j]):
                l.append(l1[i])
                i=i+1
            else:
                l.append(l2[j])
                j = j+1
    while i < len(l1):
        l.append(l1[i])
        i = i + 1
    while j < len(l2):
        l.append(l2[j])
        j = j + 1
    return l

if __name__ == "__main__":
    products = Product_service()
    products.add(Product("Apple", "Food", 3))
    products.add(Product("Laptop", "Electronics", 4500))
    products.add(Product("Banana", "Food", 2))
    products.add(Product("Phone", "Electronics", 3000))
    products.add(Product("Desk", "Furniture", 800))
    products.add(Product("Chair", "Furniture", 300))
    products.add(Product("Milk", "Food", 5))
    products.add(Product("TV", "Electronics", 2500))
    products.add(Product("Bread", "Food", 4))
    products.add(Product("Monitor", "Electronics", 1200))

    sorted_alphabetically = merge_sort(products.get_all(), key=lambda p: p._name)
    print("Sorted by name alphabetically:")
    for p in sorted_alphabetically:
        print(p)
    print ("")
    sorted_by_price = merge_sort(products.get_all(), key = lambda p: p._price, reverse=True)
    print("Sorted descending by price:")
    for p in sorted_by_price:
        print (p)