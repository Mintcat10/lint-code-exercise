#### 1047. 删除字符串中的所有相邻重复项
#### 第一个100%！！！！！！！！！！！！！！
```
执行用时 :60 ms, 在所有 python 提交中击败了69.49%的用户；
内存消耗 :12.1 MB, 在所有 python 提交中击败了100.00%的用户。
```

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for ii in S:
            if stack and ii != stack[-1]:
                stack.append(ii)
            elif stack and ii == stack[-1]:
                stack.pop()
            elif not stack:
                stack.append(ii)
        result = ''.join(stack)
        return result

作者：jun-jun-30
链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/solution/python-nei-cun-xiao-hao-ji-bai-100yong-hu-by-jun-j/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
