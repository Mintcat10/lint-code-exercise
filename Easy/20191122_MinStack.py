#### 155.最小栈
# mine
# min(list)的时间复杂度为O(N)

```列表常用操作时间复杂度
list.reverse()  O（N）
len(list)   O（1）
list(range(5))  O（N）
max(list),min(list),sum(list)   O（N）
```

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        
# better
# 思路：借用辅助栈来优化时间空间。
# https://leetcode-cn.com/problems/min-stack/solution/shi-yong-fu-zhu-zhan-tong-bu-he-bu-tong-bu-python-/
```
执行用时 :52 ms, 在所有 python 提交中击败了93.18%的用户
内存消耗 :15.4 MB, 在所有 python 提交中击败了30.61%的用户
```
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.help = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        # if not self.help:
        #     self.help.append(x)
        # if self.stack and x <= self.help[-1]:
        if not self.help or x <= self.help[-1]:
            # self.help.pop()
            self.help.append(x)
        
    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.help[-1]:
            self.help.pop()
        self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        # return min(self.stack)
        return self.help[-1]
