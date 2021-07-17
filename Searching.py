# This file has both Linear and Binary Search code.

import random

def Linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return None

def Binary_Search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            end = mid-1
        else:
            start = mid+1
    return None


def main():
    Number_list = []

    for i in range(10):
        Number_list.append(random.randint(10, 50))

    Number_list.sort()
    print(Number_list)

    res = Binary_Search(Number_list, 32)
    print(res)


if __name__ == "__main__":
    main()