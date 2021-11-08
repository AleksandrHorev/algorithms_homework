class Element:
  def __init__(self, value):
    self.value = value
    self.next:Element = None


class Stack:
    def __init__(self) -> None:
      self.first:Element = None
      self.last:Element = None

    def push(self, element: Element):
      if (self.first == None):
          self.first = element
          self.last = self.first
          return

      self.last.next = element
      self.last = element

    def pop(self):
        if(self.first == None):
            return None
        result = self.first
        self.first = self.first.next
        return result

    def isEmpty(self):
       return (self.last == None)

    def print(self):
      element = self.first
      while(element):
          print(element.value)
          element = element.next
      print('--------')

stack = Stack()
stack.push(Element(2))
stack.push(Element(3))
stack.push(Element(4))
stack.push(Element(5))
stack.print()
stack.pop()
stack.print()
print(stack.isEmpty())
print(Stack().isEmpty())