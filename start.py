#!/usr/bin/env python3
# coding=utf-8
import hashlib


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
    filepath = r'F:\ISO\cn_windows_10_business_editions_version_1909_x64_dvd_0ca83907.iso'
    with open(filepath, 'rb') as f:
        print(hashlib.sha1(f.read()).hexdigest())
