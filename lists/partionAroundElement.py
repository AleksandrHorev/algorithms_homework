# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. 
# If x is contained within the list, the values of x only need to be after the elements less than x (see below).
#  The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] 
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

class Element:
  def __init__(self, value, nextElement = None):
        self.value = value
        self.nextElement = nextElement

  def addNext(self, nextElement):
    self.nextElement = nextElement
    return self.nextElement


class Partition:
    def partiotionByElement(self, partition, list:Element):
        head = list
        tail = list
        while (list):
            next = list.nextElement
            if (list.value < partition):
                list.nextElement = head
                head = list
            else:
                tail.nextElement = list
                tail = list
            list = next

        tail.nextElement = None
        return head


addLements = [5, 4, 2, 5]
next = initialList = Element(0)
for i in range(0, len(addLements)):
  next = next.addNext(Element(addLements[i]))


res = Partition().partiotionByElement(4, initialList)
while(res):
  print(res.value)
  res = res.nextElement