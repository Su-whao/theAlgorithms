import random

def quick_sort(collection):
    '''O(nlogn)
    '''
    length = len(collection)
    if length <= 1:
        return collection
    mid = collection.pop()
    left,right = [],[]
    for c in collection:
        if c < mid:
            left.append(c)
        else:
            right.append(c)
    return quick_sort(left)+[mid]+quick_sort(right)


def quick_sort2(collection, left, right):
    '''直接修改原数组，原始的collection会被改变
    '''
    if right-left <= 1:
        return 
    mid = collection[left]
    i = left
    for j in range(left+1,right):
        if collection[j] < mid:
            collection[j],collection[i] = collection[i],collection[j]
            collection[i+1],collection[j] = collection[j],collection[i+1]
            i+=1
    quick_sort2(collection, left, i)
    quick_sort2(collection, i+1, right)
    return collection          

def quick_sort3(collection, left, right):
    if right-left <= 0:
        return
    i = left
    j = right
    mid = collection[i]
    while i<j:
        while i<j and collection[j]>mid:
            j-=1
        if i<j:
            collection[i]=collection[j]
            i+=1
        while i<j and collection[i]<mid:
            i+=1
        if i<j:
            collection[j] = collection[i]
            j-=1
    collection[i] = mid
    quick_sort3(collection,left,i-1)
    quick_sort3(collection,i+1,right)
    return collection

if __name__ == "__main__":
    collection = [random.randint(0, 1000) for i in range(10)]
    collection_sorted = quick_sort(collection)
    # print(collection_sorted)

    collection = [random.randint(0, 1000) for i in range(10)]
    collection_sorted = quick_sort2(collection,0,len(collection))
    # print(collection_sorted)

    collection = [random.randint(0, 1000) for i in range(10)]
    collection_sorted = quick_sort3(collection, 0, len(collection)-1)
    print(collection_sorted)
