#!/usr/bin/env python3
# coding=utf-8


def twoSum(nums, target):
    dict_num = {}
    for i in range(len(nums)):
        if target - nums[i] in dict_num:
            return [(i, nums[i]),
                    (dict_num[target - nums[i]],
                     nums[dict_num[target - nums[i]]])]
        dict_num[nums[i]] = i
    return None


if __name__ == "__main__":
    nums = [2, 3, 5, 7, 9, 10]
    print(twoSum(nums, 11))
    print(1 + 2 + 3)
