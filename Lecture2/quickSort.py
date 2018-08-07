# -*- coding: utf-8 -*-
"""
@ Time   : 2018/8/7 11:49
@ Author : huayuan
"""

def quickSort(arr):
    if (len(arr) <= 1):
        return arr
    mid = arr[(len(arr) // 2)];
    left = [x for x in arr if x < mid]
    middle = [x for x in arr if x == mid]
    right = [x for x in arr if x > mid]
    return quickSort(left) + middle + quickSort(right)

if __name__ == "__main__":
    print(quickSort([4,2,3,1]))
    print(quickSort([-23,34,45,1]))
