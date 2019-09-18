#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-18 11:49:08
# @Author  : Slade_zhang slade.zhang@qq.com

#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

import os
class  Solution(object):
	"""docstring for  Solution"""
	def twoSum(self, nums, target):
		sorted_id = sorted(range(len(nums)), key = lambda k: nums[k])
		head = 0
		tail = len(nums) - 1
		sum_result = nums[sorted_id[head]] +nums[sorted_id[tail]]
		while sum_result != target:
			if sum_result > target:
				tail -= 1
			elif sum_result < target:
				head += 1
			sum_result = nums[sorted_id[head]] +nums[sorted_id[tail]]
		return ([sorted_id[head], sorted_id[tail]])

a = Solution()
a.twoSum([2,4,11,3,5,12],23)

