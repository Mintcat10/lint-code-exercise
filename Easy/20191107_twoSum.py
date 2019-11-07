#### 1. 两数之和 20191107
# mine 
# Time:6216ms Memory:12.4MB Complexity:O(n^2)
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index_x,ii in enumerate(nums):
        for index_y,jj in enumerate(nums):
            if index_x == index_y:
                continue
            if ii + jj == target:
                return [index_x,index_y]
# better 
# 关键主要是想找到 num2 = target - num1，是否也在 list 中
# Complexity:O(n) Time:1636ms
def twoSum(nums, target):
    lens = len(nums)
    j=-1
    for i in range(lens):
        if (target - nums[i]) in nums:
            if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                continue
            else:
                j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2                
                break
    if j>0:
        return [i,j]
    else:
        return []
# better pro
# 查找并不需要每次从 nums 查找一遍，只需要从 num1 位置之前或之后查找即可。但为了方便 index 这里选择从 num1 位置之前查找
# Complexity:O(n) Time:652ms
def twoSum(nums, target):
    lens = len(nums)
    j=-1
    for i in range(1,lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j>=0:
        return [j,i]
# 字典查找法
# Complexity:O(n) Time:88ms
def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]
# 字典查找法 pro
# Complexity:O(n) Time:70ms
def twoSum(nums, target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i,hashmap.get(target - num)]
        hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
