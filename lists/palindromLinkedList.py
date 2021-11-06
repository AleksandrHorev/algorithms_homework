# Palindrome: Implement a function to check if a linked list is a palindrome.
class Element:
  def __init__(self, value, nextElement = None):
        self.value = value
        self.nextElement = nextElement

  def addNext(self, nextElement):
    self.nextElement = nextElement
    return self.nextElement


class List:
    def isPalindrom(self, node:Element):
        if (not node.nextElement):
          return True

        slowPointer = node
        fastPointer = node
        stack = []
        while (fastPointer):
            if(slowPointer.nextElement and fastPointer.nextElement and fastPointer.nextElement.nextElement):
               stack.append(slowPointer.value)
               slowPointer = slowPointer.nextElement
               fastPointer = fastPointer.nextElement.nextElement
               continue

            if(slowPointer.nextElement and fastPointer.nextElement):
                stack.append(slowPointer.value)
                slowPointer = slowPointer.nextElement
                fastPointer = None
                continue
            fastPointer = None
        while(slowPointer):
          if(not stack or slowPointer.value != stack.pop()):
            return False
          slowPointer = slowPointer.nextElement
        
        if(len(stack) != 0):
          return False
        return True

# addLements = [5, 2, 2, 5, 0]
addLements = [3, 5, 2, 0, 2, 5, 3, 0]
# addLements = [3, 5, 2, 2, 5, 3, 0, 0]
# addLements = [3, 5, 2, 2, 5, 3, 0]
# addLements = []
# addLements = [5, 2, 2, 5, 5, 0]
next = initialList = Element(0)
for i in range(0, len(addLements)):
  next = next.addNext(Element(addLements[i]))


print(List().isPalindrom(initialList))