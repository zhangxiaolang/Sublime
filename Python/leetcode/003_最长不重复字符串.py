#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-18 15:15:11
# @Author  : Slade_zhang slade.zhang@qq.com

#给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
import os
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans;

a = Solution()
print(a.lengthOfLongestSubstring('abcacdec'))

