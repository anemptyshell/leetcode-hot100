#  s = "cbaebabacd", p = "abc"
# 输出: [0,6]
from typing import List


## 时间复杂度：O（n），其中n是字符串 s 的长度。代码只需要对字符串 s 进行一次遍历，每次操作字符计数列表的时间复杂度为 O（1）
## 空间复杂度：O（1），因为字符计数列表的长度固定为 26，不随输入字符串的长度变化而变化
## 在Python中，可以使用内置的ord()函数将字符转换为ASCII码，使用chr()函数将ASCII码转换为字符。
class Solution:
    def findAnagrams(self, s: str, p: str) -> List:
        n, m = len(s), len(p)
        res = []
        if n < m:
            return res        
        p_count = [0]*26
        window_count = [0]*26
        
        left = 0
        for char in p:
            p_count[ord(char) - ord('a')] += 1
        
        for right in range(n):

            window_count[ord(s[right]) - ord('a')] += 1
            if right-left+1 == m:
                if window_count == p_count:
                    res.append(left)
                window_count[ord(s[left]) - ord('a')] -= 1
                left += 1
            
        return res
            


solution = Solution()
s = "cbaebabacd"
p = "abc"
print(solution.findAnagrams(s, p))  # 输出: [0, 6]


# a = [0] * 5
# print(a)  ## [0, 0, 0, 0, 0]



# 时间复杂度：O((len(s) - n + 1)*nlogn)，其中 len(s) 是字符串 s 的长度，n 是字符串 p 的长度。
# 因为每次对长度为 n 的子串进行排序的时间复杂度是 nlogn ，外层循环需要遍历 len(s) - n + 1 次。
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List:
#         n = len(p)
#         result = []
     
#         for left in range(len(s) - n + 1):
#             right = left + n -1
#             res = ''.join(sorted(s[left:right + 1]))
#             if res == p:
#                 result.append(left)
            
#         return result

                      
            

