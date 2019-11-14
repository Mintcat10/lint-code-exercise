#### 13. 罗马数字转整数
# mine
# 照搬 12 题（replace真好用）
```
执行用时 :48 ms, 在所有 python 提交中击败了70.08%的用户
内存消耗 :11.8 MB, 在所有 python 提交中击败了15.53%的用户
```

def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    Characters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    change = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = 0
    for index,i in enumerate(Characters):
        while i == s[:len(i)]:
            s = s.replace(i,'',1)
            result += change[index]
        if len(s)==0:
            return result
