# not optimal, can do without additional array
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        arr = []
        while(node):
            arr.append(int(node.val))
            node = node.next
        result = 0
        nextNumber = 1
        for el in arr[::-1] :
            if (el != 0):
                result += nextNumber
            nextNumber = nextNumber * 2
        
        return result
        