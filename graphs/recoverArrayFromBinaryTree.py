# 4.9 Cracking the coding int
# BST Sequences: A binary search tree was created by traversing through an array from left to right 
# and inserting each element. Given a binary search tree with distinct elements, print all possible arrays
#  that could have led to this tree.

from queue import LifoQueue, Queue

class Node:
    def __init__(self, value):
        self.value = str(value)
        self.left: Node = None
        self.right: Node = None
        self.deep = None

# doesn't work
class ArrayFromBST:
    def __init__(self):
      self.array = []

    def recoveryArray(self, root: Node):
        if (not root): return ''

        queue = Queue()
        queue.put(root)
        reversedQueue = self.bfs(queue)
        self.printArray()

        firstFromEnd = None
        while (not reversedQueue.empty()):
            firstFromEnd = firstFromEnd or reversedQueue.get()
            if (not reversedQueue.empty()): 
                secondFromEnd = reversedQueue.get()

            if (firstFromEnd.deep == secondFromEnd.deep):
                self.array.pop()
                self.array.pop()
                queue.put(firstFromEnd)
                queue.put(secondFromEnd)
                self.bfs(queue)
                self.printArray()

                firstFromEnd = None
                secondFromEnd = None
            else: 
                firstFromEnd = secondFromEnd
                secondFromEnd = None
                self.array.pop()
                self.array.pop()
                self.array.pop()

    def bfs(self, queue):
      deep = 1
      reversedQueue = LifoQueue()
      while(not queue.empty()):
          node = queue.get()
          deep += 1
          self.array.append(node)
          if (node.left): 
              node.left.deep = deep
              queue.put(node.left)
              reversedQueue.put(node.left)
          if (node.right):
              node.right.deep = deep
              queue.put(node.right)
              reversedQueue.put(node.right)
      
      return reversedQueue

    def printArray(self):
        str = ''
        for el in self.array:
            str += el.value
        print(str)


root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(6)

# doesn't work
ArrayFromBST().recoveryArray(root)

