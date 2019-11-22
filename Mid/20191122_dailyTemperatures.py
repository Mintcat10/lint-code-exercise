#### 739.每日温度
# mine
# 超过时间限制：28/37
def dailyTemperatures(self, T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    stack = []
    day_len = len(T)
    print(day_len)
    for current in range(day_len):
        day = 1
        index = 1
        # print(current,stack)
        # 判断T中最后一个元素
        if index+current == day_len:
            day -= 1 
            stack.append(day)
            break
        while T[current] >= T[index+current]:
            day += 1
            index += 1
            # print(day + current,day_len,index+current)
            if day + current == day_len:
                day = 0
                break
        stack.append(day)
    return stack

# office
# https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode/
# 思路：从后往前，记录每个有用信息（比前面的值大的位置）的index，当信息无用时（被新的信息替代），删除无用信息并记录删除个数作为输出结果。
```
我们用栈记录索引，满足 T[stack[-1]] < T[stack[-2]] < ...，其中 stack[-1] 是栈的顶部，stack[-2] 是从顶部开始的第二个元素，依此类推；我们将在处理每个 T[i] 时保持 stack[-1] > stack[-2] > ...。
我们通过当前温度和栈顶索引所代表的温度比较来找到温度升高的位置。
```
```
执行用时 :404 ms, 在所有 python 提交中击败了100.00%的用户
内存消耗 :15.3 MB, 在所有 python 提交中击败了27.78%的用户
```
```
时间复杂度：O(N)O(N)。其中 NN 是 T 的长度，每个索引最多做一次压栈和出栈的操作。
空间复杂度：O(W)O(W)，其中 WW 是 T[i] 的可取值的数目。
```
def dailyTemperatures(self, T):
  len_T = len(T)
  ans = [0] * len_T
  stack = [] # 存储value为index
  for i in range(len_T-1,-1,-1):
      while stack and T[i] >= T[stack[-1]]:
          stack.pop()
      if stack:
          ans[i] = stack [-1] - i
      stack.append(i)
  return ans
