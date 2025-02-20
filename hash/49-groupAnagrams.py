from typing import List

## 字母异位词分组

## Python的sorted()函数可以对字符串中的字符进行排序。这个函数返回一个新的列表，列表中包含了原字符串中所有字符的有序序列。
## 通过将sorted()函数的结果与join()函数结合使用，我们可以得到一个排序后的字符串。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if not strs:
        #     return [strs]
        
        hash_map = {}
        
        for word in strs:
            key = ''.join(sorted(word))

            if key in hash_map:
                hash_map[key].append(word)
            else:
                hash_map[key] = [word]
            
        return list(hash_map.values())
        