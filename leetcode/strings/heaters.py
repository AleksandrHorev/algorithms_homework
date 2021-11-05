# https://leetcode.com/problems/heaters/
# 475. Heaters

class Solution:
    def findRadius(self, houses, heaters):
      heaters = sorted(heaters) + [float('inf')]
      i = r = 0
      for x in sorted(houses):
          while x >= sum(heaters[i:i+2]) / 2.:
              i += 1
          r = max(r, abs(heaters[i] - x))
      return r

print(Solution().findRadius([1,2,3], [2])) #"1
print(Solution().findRadius([1,2,3], [4])) #"3
print(Solution().findRadius([2,3,4], [1])) #"3
print(Solution().findRadius([1, 3, 8, 10], [4])) #6
print(Solution().findRadius([2,4], [1])) #"3
print(Solution().findRadius([2, 4, 10, 20, 31], [1, 4, 40])) #16
print(Solution().findRadius([1,2,3,4], [1,4])) #1
print(Solution().findRadius([1,1,1,1,1,1,999,999,999,999,999],[499,500,501])) #498
print(Solution().findRadius([474833169,264817709,998097157,817129560],
[197493099,404280278,893351816,505795335])) #104745341 , 3-3
print(Solution().findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612])) #161834419
