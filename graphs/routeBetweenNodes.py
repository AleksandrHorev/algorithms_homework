# 4.1 Cracking the coding int
# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

# support class
class Element:
  def __init__(self, value):
    self.value = value
    self.next:Element = None

class Queue:
    def __init__(self) -> None:
      self.first:Element = None
      self.last:Element = None

    def push(self, element):
      if (self.first == None):
          self.first = Element(element)
          self.last = Element(element)
          self.first.next = self.last
          return

      self.last.next = Element(element)
      self.last = Element(element)

    def pop(self):
        if(self.first == None):
            return None
        result = self.first
        if (self.first != self.first.next):
            self.first = self.first.next
        else:
          self.first = None
        return result

    def isEmpty(self):
      return (self.last == None)


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def addChild(self, node):
        self.children.append(node)

    def setParent(self, parent):
        self.parent = parent

# the solution is fine. the problem in implementation Queue (pop doesn't work correctly)
class Solution:
    def searchRoute(self, root: Node, firstNode: Node, secondNode: Node,) -> Node:
        queue: Queue = Queue()
        queue.push(root)
        path = []
        while(not queue.isEmpty()):
            node = queue.pop().value
            for child in node.children:
                child.setParent(node)
                if (node == secondNode):
                  queue.last = None
                  break
                queue.push(child)

        pathNode = secondNode
        while(pathNode != firstNode):
          path.append(pathNode.value)
          pathNode = pathNode.parent
        path.append(firstNode.value)
        return path


root = Node(0)
firstNode = Node(1)
secondNode = Node(7)
firstNode.addChild(Node(4))
firstNode.addChild(Node(5))
firstNode.children[1].addChild(secondNode)
root.addChild(Node(2))
root.addChild(firstNode)
print(Solution().searchRoute(root, firstNode, secondNode).value)




