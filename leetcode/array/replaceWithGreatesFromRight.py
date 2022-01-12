# 1299. Replace Elements with Greatest Element on Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arrLen = len(arr)
        max = arr[arrLen - 1]
        arr[arrLen - 1] = -1
        for i in range(arrLen - 2, -1, -1):
            possibleMax = arr[i]
            arr[i] = max
            if (possibleMax > max):
                max = possibleMax
        
        return arr
            