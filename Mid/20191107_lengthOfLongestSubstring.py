# 3. 无重复字符的最长子串 
# mine
# 思路：遍历字符串，将符合要求子序列加入列表
# Complexity:O(n!) Top:5% Time:1016ms Memory:26.3MB 
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    all_str = []
    j = 0
    a = ''
    while j + len(a)< len(s):
        a = ''
        for index,ii in enumerate(s[j:]):
            # print('a',a,ii)
            if ii not in a:
                a += ii
            else:
                all_str.append(a)
                j += 1
                break
            # 字符串最后两位相同情况下，陷入死循环
            if j == len(s) - 1:
                all_str.append(a)
                j += 1
                break
            # 确保最后一个a添加入all_str
            if j + len(a) == len(s):
                all_str.append(a)
                j += 1
                break 
    len_s = [len(ii) for ii in all_str]
    result = max(len_s)
    return result

# other
# O(n)
# 主要用到思路是：滑动窗口
'''
 其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
如何移动？
我们只要把队列的左边的元素移出就行了，直到满足题目要求！
一直维持这样的队列，找出队列出现最长的长度时候，求出解！
'''
def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:return 0
    left = 0
    lookup = set()
    n = len(s)
    max_len = 0
    cur_len = 0
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:max_len = cur_len
        lookup.add(s[i])
    return max_len
