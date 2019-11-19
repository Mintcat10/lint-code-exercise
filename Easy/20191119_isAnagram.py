#### 242. 有效的字母异位词
# mine
```
执行用时 :236 ms, 在所有 python 提交中击败了5.26%的用户
内存消耗 :12.6 MB, 在所有 python 提交中击败了36.40%的用户
```
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    # for i in s:
    #     if i in t:
    #         pass
    #     else:
    #         return False

    # for i in t:
    #     if i in s:
    #         pass
    #     else:
    #         return False
    # return True

    # print(len(s),len(t))
    # print(type(s),type(t)) # (<type 'unicode'>, <type 'unicode'>) 
    # print(type(s.encode('utf-8')),type(t.encode('utf-8'))) # (<type 'str'>, <type 'str'>)
    s = s.encode('utf-8')  
    t = t.encode('utf-8') # 不转换耗时672 ms
    # while len(s) != 0 or len(t) != 0:

    for i in s:
        if i in t:
            s = s.replace(i,'',1)
            t = t.replace(i,'',1)
            # s = s.translate(str.maketrans('','',i))
            # s = t.translate(str.maketrans('','',i)) 一次删除所有相同元素，判断剩余字符串长短，应该可以提速，但提示str.maketrans报错
            if len(s) != len(t):
                return False
        else:
            return False
    print(s,t)
    # if len(s) != 0 or len(t) != 0:
    if len(t) != 0:
        return False
    return True
    
 # better_1:官方
 # 思路:直接排序字符串，判断是否相等。
 # 复杂度：O(nlogn)
 
 # better_2:
 # 思路：利用set()函数，减少循环次数，判断s.count()和t.count()长度。
 # https://leetcode-cn.com/problems/valid-anagram/solution/zhan-sheng-98de-python-jie-fa-by-reynard/
 
 # better_3
 # return sorted(s)==sorted(t)
 # https://leetcode-cn.com/problems/valid-anagram/solution/pai-xu-shu-zu-ji-lu-ge-shu-by-powcai/
 
 # better_4
 # return collections.Counter(s) == collections.Counter(t)
 # https://leetcode-cn.com/problems/valid-anagram/solution/python-yi-xing-ji-bai-9992-de-yong-hu-by-baiyizhe/
 
    
    
