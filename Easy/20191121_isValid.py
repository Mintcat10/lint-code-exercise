#### 20. 有效的括号

# mine
# 。。。。
# 思路：'(','[','{' 三个半括号比在偶数位置
# 卡在第54,55个提交项 '{[}]','{[]}'
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    # s = s.encode('utf-8')
    # s_len = len(s)
    # if s_len % 2 != 0:
    #     return False
    # dict_ = {'(':')','[':']','{':'}'}
    # jump = 1
    # for ii in range(0,s_len,2):

    #     try:
    #         half_s = dict_[s[ii-jump+1]]
    #     except:
    #         print('1111')
    #         return False

    #     jump = 1
    #     jump_s = s[ii+1]
    #     while jump_s in ['(','[','{']:
    #         jump += 1
    #         try:
    #             jump_s = s[ii+jump]
    #         except:
    #             print('2222')
    #             return False
    #         print('jump',jump)

    #     print(half_s,s[(ii-jump+1)+1+(jump-1)*2])
    #     print(type(half_s),type(s[(ii-jump+1)+1+(jump-1)*2]))
    #     if half_s == s[(ii-jump+1)+1+(jump-1)*2]:
    #         pass
    #     else:
    #         print('3333')
    #         return False
    # return True

# 捷径（正确的来说，每次都能去掉一对括号，最后就成了空）
def isValid(self, s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''

# 官方
# https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode/
# 思路：栈
```
执行用时 :16 ms, 在所有 python 提交中击败了95.68%的用户
内存消耗 :11.9 MB, 在所有 python 提交中击败了20.52%的用户
```
def isValid(self, s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for ii in s:
        if ii in mapping:
            # index==0时不会进入此处，所以可以这样赋值
            tmp = stack.pop() if stack else '#'
            if tmp != mapping[ii]:
                return False
        else:
            stack.append(ii)
    return stack == []


