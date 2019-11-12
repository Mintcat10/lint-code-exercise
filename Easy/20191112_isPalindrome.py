# 9. 回文数
# mine
# Time: 56ms  Top:1 - 75.86%
# Memory:11.7MB Top:1 -27.5%
# Complexity:O(str)
# 思路：利用字符串翻转的快捷操作
def isPalindrome(self, x):
	"""
	:type x: int
	:rtype: bool
	"""
	if x < 0 :
		return False
	x_str = str(x)
	x_palindyime = x_str[::-1]
	if x_str == x_palindyime:
		return True
	else:
		return False
		
# mine 
# 参考https://leetcode-cn.com/problems/palindrome-number/solution/hui-wen-shu-by-leetcode/
# Time: 60ms  Top:1 - 65.86%
# Memory:11.7MB Top:1 -27.5%
```
	复杂度分析
	时间复杂度：O(log 10​(n))    对于每次迭代，我们会将输入除以10，因此时间复杂度为 O(log_{10}(n))O(log 10​ (n))。
	空间复杂度：O(1)。
```
def isPalindrome(self, x):
	"""
	:type x: int
	:rtype: bool
	"""
	# 排除 x = 1、21120的情况
	if x < 0 or ( x%10== 0  and x !=0):
		return False
	elif x >= 0 and x < 10 :
		return True

	x_end = 0
	# while x_end < x and x > 9:
	while x_end < x and x > 9:
		x_mod = x % 10
		x_end = x_mod + 10 * x_end

		# 两个if，保证 x = 121、1221的情况都可以相等
		# PS:参考官方答案更优美
		if x == x_end:
			return True

		x = x // 10

		if x == x_end:
			return True
	   #  x = x // 10
	return False
