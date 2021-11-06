# Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
# Return the inter­ secting node. Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference)
#  as the jth node of the second linked list, then they are intersecting.
class Element:
  def __init__(self, value, nextElement = None):
        self.value = value
        self.nextElement = nextElement

  def addNext(self, nextElement):
    self.nextElement = nextElement
    return self.nextElement


class List:
    def getIntersection(self, firstNode:Element, secondNode:Element):
        if (not firstNode or not secondNode):
          return None
        map = {}
        while(firstNode):
            map[firstNode] = '1'
            firstNode = firstNode.nextElement
        while(secondNode):
          if (map.get(secondNode)):
            return secondNode
          secondNode = secondNode.nextElement
        return None


addLements = [3, 5, 2, 0, 2, 5, 3, 0]
addLements2 = [1,5,2]
elem = Element(8)
next = initialList = Element(0)
for i in range(0, len(addLements)):
  next = next.addNext(Element(addLements[i]))
initialList.addNext(elem)

next = initialList2 = Element(0)
for i in range(0, len(addLements2)):
  next = next.addNext(Element(addLements2[i]))
initialList2.addNext(elem)


print(List().getIntersection(initialList, initialList2))