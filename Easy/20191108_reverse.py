#### 7.整数反转
# mine
# Time: 16ms  Top:1 - 95.24%
# Memory:12.4MB Top:1 -9.55%
# Complexity:O(n)
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
     x_str = str(x)
    if x > 0:
		x_tmp = x_str[::-1]
        x_tmp = int(x_tmp)
    elif x < 0:
        x_str = x_str[1:]
        x_tmp = x_str[::-1]
        x_tmp = -int(x_tmp)
    elif x == 0:
        x_tmp = 0
    if x_tmp > 2**31 or x_tmp < -2**31: 
        x_tmp = 0
    return x_tmp
