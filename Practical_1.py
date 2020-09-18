import numpy as np


def selection_sort(a):
    a = list(a)
    sortedarray = []
    for i in range(0, len(a)):
        sortedarray.append(min(a))
        a.pop(a.index(min(a)))

    return np.asarray(sortedarray)


test1 = np.array([1, 4, 6, 3, 5, 4, 2])
result1 = selection_sort(test1)
print(result1)

def bubble_sort(b):
    re = True
    while re:
        re = False
        for j in range(0, len(b)-1):
            if b[j] > b[j+1]:
                for i in range(0, len(b)-1):
                    if b[i] > b[i+1]:
                        b[i], b[i+1] = b[i+1], b[i]
                re = True
                break
    return b
test2 = np.array([1, 4, 6, 3, 5, 4, 2])
result2 = bubble_sort(test2)
print(result2)


def insertion_sort(c):
    l=[]
    for i in range(len(c)-1):
        l.append(i)
        for j in l:
            if c[i+1] <= c[j]:
                c[j],c[i+1]=c[i+1],c[j]
            else:
                continue
    return c
test3=np.array([1, 4, 6, 3, 5, 4, 2])
result3 = insertion_sort(test3)
print(result3)


#def quick_sort(d):
