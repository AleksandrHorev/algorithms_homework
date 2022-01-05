class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        map1 = self.getMap(nums1)
        map2 = self.getMap(nums2)
        map3 = self.getMap(nums3)
        map12 = self.mergeMaps(map1, map2)
        map13 = self.mergeMaps(map1, map3)
        map23 = self.mergeMaps(map2, map3)
        
        result = map12 | map13 | map23
                
        return list(result)
    
    def getMap(self, arr):
        map = {}
        for num in arr:
            map[num] = 1  
        return map
    
    def mergeMaps(self, firstMap, secondMap):
        map = {}
        for key in firstMap:
            if(secondMap.get(key)):
                map[key] = 2
        return map