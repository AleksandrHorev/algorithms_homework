# 4.8 Cracking the coding int
# First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes 
# in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

from enum import Enum
class Path(Enum):
    FIRST = 1
    SECOND = 2

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.path = []

    def addChild(self, node):
        self.children.append(node)

    def setParent(self, parent):
        self.parent = parent

class CommonAncestor:
    def markNodePaths(self, node:Node, firstNode:Node, secondNode:Node):
        if (not node): return None

        if (node == firstNode):
            return Path.FIRST
        if (node == secondNode):
             return Path.SECOND
        if (len(node.children) == 0):
            return False
        for child in node.children:
            result = self.markNodePaths(child, firstNode, secondNode)
            if (result): node.path.append(result)

    def findChildrenWithPath(self, node:Node):
        for child in node.children:
          if(len(child.path) > 1):
            return child

    def findPath(self, root:Node):
      node = root
      path = []
      while (node and len(node.path) > 1):
        path.append(node.value)
        node = self.findChildrenWithPath(node)
      return path


    def findCommonAncestor(self, root:Node, firstNode:Node, secondNode:Node) -> Node:
      root.path = [Path.FIRST, Path.SECOND]
      self.markNodePaths(root, firstNode, secondNode)
      result = self.findPath(root)
      return result


nodes = Node(0)
nodes.addChild(Node(9))
first = Node(1)
second = Node(10)
nodes.addChild(Node(2))
nodes.addChild(Node(3))
nodes.addChild(Node(7))
nodes.addChild(Node(5))
nodes.addChild(Node(6))
nodes.children[2].addChild(second)
nodes.children[2].addChild(first)
nodes.children[2].children[0].addChild(first)
nodes.children[2].addChild(Node(8))
print(CommonAncestor().findCommonAncestor(nodes, first, second))

