# -*- coding:utf-8 -*-
import random


def merge_sort(collection, left=None, right=None, temp=[]):
    '''归并排序
    '''
    print(left,right)
    # if left == 2:
    #     exit
    if left == None:
        left = 0
    if right == None:
        right = len(collection)

    if right - left <= 1:
        return collection[left:right]
    mid = (right+left) // 2

    left_coll = merge_sort(collection, left, mid)
    right_coll = merge_sort(collection, mid, right)

    # merge
    while right_coll and left_coll:
        print('--')
        print(left_coll, right_coll, temp)
        if right_coll[-1] < left_coll[-1]:
            t = left_coll.pop()
            temp.append(t)
            print(len(left_coll))
        else:
            t = right_coll.pop()
            temp.append(t)
            print(len(left_coll))

    if not left_coll:
        right_coll.reverse()
        temp.extend(right_coll)
    else:
        left_coll.reverse()
        temp.extend(left_coll)
    temp.reverse()
    return temp

if __name__ == "__main__":
    collection = [random.randint(1,100) for _ in range(10)]
    print(collection)
    collection_sorted = merge_sort(collection)
    print(collection_sorted)
