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

# better
# 思路：利用字典，复杂度为O(1) 
# 字典构造十分巧妙。
# 参考链接：https://leetcode-cn.com/problems/roman-to-integer/solution/2-xing-python-on-by-knifezhu/
···
代码行数：解析
构建一个字典记录所有罗马数字子串，注意长度为2的子串记录的值是（实际值 - 子串内左边罗马数字代表的数值）

这样一来，遍历整个 ss 的时候判断当前位置和前一个位置的两个字符组成的字符串是否在字典内，如果在就记录值，不在就说明当前位置不存在小数字在前面的情况，直接记录当前位置字符对应值

举个例子，遍历经过 IVIV 的时候先记录 II 的对应值 11 再往前移动一步记录 IVIV 的值 33，加起来正好是 IVIV 的真实值 44。max 函数在这里是为了防止遍历第一个字符的时候出现 [-1:0][−1:0] 的情况
···
def romanToInt(self, s: str) -> int:
    d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
    return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s)) 
