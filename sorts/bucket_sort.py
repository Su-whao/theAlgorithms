'''
将collection根据 映射规则 分成 N 个桶
对每个桶分别进行排序
然后进行组合

可以发现桶排序的效率与桶的划分方法和映射规则有直接关系
映射规则与桶的个数相关

如果桶的个数很大，则桶排序效率趋近于计数排序
如果桶的个数很少，比如1个桶，则桶排序效率趋近于桶内排序算法的效率
'''
import random

def bucket_sort(collection):
    '''
    生成桶的方法：生成 max_num//10 - min_num//10+1 个桶
    这里选择的映射方法： num // 10 - min_num // 10，这样可以保证第一个桶的每个
    数字都是比第二个桶的数字小的，这样在合并的时候就很方便
    '''
    min_num, max_num = min(collection), max(collection)
    bucketArr = [[] for i in range(max_num//10-min_num//10+1)]
    for i in collection:
        index = i // 10 - min_num // 10
        bucketArr[index].append(i)
    collection.clear()
    for i in bucketArr:
        i.sort()
        collection.extend(i)
    return collection

if __name__ == "__main__":
    collection = [random.randint(1,100) for _ in range(100)]
    collection_sorted = bucket_sort(collection)
    # print(collection_sorted)