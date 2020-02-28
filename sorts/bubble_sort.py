import random

def bubble_sort(collection):
    c_lens = len(collection)
    c = 0
    for i in range(1,c_lens):
        for j in range(i):
            c += 1
            if collection[i] < collection[j]:
                collection[i],collection[j] = collection[j],collection[i]
    print(c)
    return collection


def bubble_sort2(collection):
    length = len(collection)
    c = 0
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            c+=1
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    print(c)
    return collection

if __name__ == "__main__":
    collection = [random.randint(1,100) for _ in range(10)]
    collection_sorted = bubble_sort(collection)
    # print(collection_sorted)
    collection = [random.randint(1, 100) for _ in range(10)]
    collection_sorted = bubble_sort2(collection)
    # print(collection_sorted)
