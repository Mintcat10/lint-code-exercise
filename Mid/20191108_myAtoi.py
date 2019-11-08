#### 8. 字符串转换整数
# fuck you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
  输入:
  "   +0 123"
  输出
  123
  stdout
  ('1111', '', 1)
  ('1111', '', 2)
  ('1111', '', 3)
  ('2222', u'+', 3)
  ('3333', u'+', 4)
  ('2222', u'+0', 4)
  ('1111', u'+0', 6)
  ('3333', u'+0', 6)
  ('2222', u'+01', 6)
  ('3333', u'+01', 7)
  ('2222', u'+012', 7)
  ('3333', u'+012', 8)
  ('2222', u'+0123', 8)
  +0123
  ('@@ re', 123)
  预期结果
  0
'''
class Solution(object):
  def myAtoi(self, str):
      """
      :type str: str
      :rtype: int
      """
      j = 0
      s_len = len(str)
      s_result = ''
      if s_len == 0:
          return 0
      while s_len != j:
          s_tmp = str[j]
          if s_tmp == ' ' :
              j += 1
              print('1111',s_result,j)
              continue 
          elif s_tmp == '-' or s_tmp == '+':
              # if str[j+1] == ' ':
              #     continue
              try:
                  s_num = int(str[j+1])
                  s_useful = str[j]
              except:
                  return 0
          else:
              try:
                  s_num = int(str[j])
                  s_useful = str[j]
                  print('3333',s_result,j)
              except:
                  try:
                      return int(s_result)
                  except:
                      return 0
          s_result += s_useful
          print('2222',s_result,j)
          j += 1
      print(s_result)
      try:
          re = int(s_result)
          print('@@ re',re,)
          if re < -2**31 or re > 2**31:
              return -2**31
          return re
      except:
          return 0

# 正确思路: 使用正则表达式
def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
################################## 以后十五分钟还没有得到正确结果,马上放弃!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
