# https://leetcode.com/problems/find-and-replace-in-string/
# 833. Find And Replace in String

from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        lenghtIndices = len(indices)
        map = []
        for i in range(0, lenghtIndices):
            map.append([indices[i], sources[i], targets[i]])

        print(map)
        map.sort(reverse=True)
        print(map)
        for i in range(0, lenghtIndices):
            lenghtSourcesI = len(map[i][1])
            if (s[map[i][0]:(map[i][0] + lenghtSourcesI)] == map[i][1]):
                s = s[:map[i][0]] + map[i][2] + s [(map[i][0] + lenghtSourcesI):]
        return s

print(Solution().findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"])) #"eeebffff"
print(Solution().findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"])) #"vbfrssozp"

#  imrpvoing - use list instead of string s (s is immutablem list is mutable). not reverse array, add targets and efter remove old symbols