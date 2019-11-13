# 11. 盛最多水的容器
# mine
# 思路：暴力破解，答案提交当len==5000时候超出时间限制，但结果计算正确。
# 42/50 个通过测试用例
```
  时间复杂度：O(n^2)
  空间复杂度：O(1)
```
def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    print('#### len',len(height))
    h_len = len(height)
    if h_len == 1:
        return 0
    container = []
    for ii in  range(1,h_len):
        for jj in range(h_len):
            if jj+ii == h_len:
                container_tmp = 0
                container.append(container_tmp)
                break
            else:
                container_tmp = (ii) * min(height[jj],height[jj+ii])
                container.append(container_tmp)
    return max(container)

# 简洁版暴力破解
# 参考：https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode/
# 超出时间限制，结果无误。同样在len == 5000时候。
def maxArea(self, height):
  maxarea = 0
  h_len = len(height)
  print(h_len)
  for ii in range(h_len):
      for jj in range(ii+1,h_len):
          maxarea = max(maxarea, min(height[ii], height[jj]) * (jj - ii))
  return maxarea

# better
# 双指针法
```
执行用时 :104 ms, 在所有 python 提交中击败了96.86%的用户
内存消耗 :13.2 MB, 在所有 python 提交中击败了10.41%的用户
时间复杂度：O(n)O(n)，一次扫描。
空间复杂度：O(1)O(1)、
```
def maxArea(self, height):
  maxarea = 0
  l = 0
  r = len(height) - 1
  while l < r:
      maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
      if height[l] < height[r]:
          l += 1
      else:
          r -= 1
  return maxarea
  

    
