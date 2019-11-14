# 12. 整数转罗马数字
# mine
# 列表思路参考：https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-cong-zui-gao-wei-kai/

```
执行用时 :32 ms, 在所有 python 提交中击败了94.83%的用户
内存消耗 :11.7 MB, 在所有 python 提交中击败了27.70%的用户
```
def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    Characters = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    Characters = Characters[::-1]
    change = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    change = change[::-1]
    Roman = ''

    for index,i in enumerate(change):
        while num >= i:
            num = num - i
            Roman += Characters[index]
        if num == 0:
            return Roman
    return Roman
