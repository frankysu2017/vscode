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


def get_iso_sha1(filename):
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


if __name__ == "__main__":
    # print(get_iso_sha1(filepath))
    print(hashlib.md5('Hello, world1!'.encode('utf8')).hexdigest())
