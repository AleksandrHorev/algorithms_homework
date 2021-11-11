# 4.7 Cracking the coding int
# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
# where the second project is dependent on the first project). All of a project's dependencies must be built before
# the project is. Find a build order that will allow the projects to be built. If there is no valid build order,
# return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) Output: f, e, a, b, d, c

from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def addChild(self, node):
        self.children.append(node)

    def setParent(self, parent):
        self.parent = parent

class Dependence:
    def __init__(self, main, dependent):
        self.main = main
        self.dependent = dependent

class BuildOrder:
    def getOrder(self, allProjects, dependencies):
      nodes = {}
      roots = {}
      for project in allProjects:
          nodes[project] = Node(project)
          roots[nodes[project]] = '1'

      for dependence in dependencies:
          main = nodes[dependence.main]
          dependent = nodes[dependence.dependent]
          if(roots.get(dependent)): roots.pop(dependent)
          main = main.addChild(dependent)

      if(not len(roots)): return 'Can not construct an order'

      result = []
      for root in roots:
        
        queue = Queue()
        queue.put(root)
        while(not queue.empty()):
            node = queue.get()
            result.append(node)
            for child in node.children:
              if (roots.get(child)): return 'Can not construct an order. Theres is a cicl.'

              if (nodes.get(child.value)):  # we don't want duplicate 
                  queue.put(child)
                  nodes.pop(child.value)
              

      return result


allProjects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [Dependence('a', 'd'), Dependence('f', 'b'), Dependence('b', 'd'), Dependence('f', 'a'), Dependence('d', 'c')]
result = BuildOrder().getOrder(allProjects, dependencies)
for res in result: print(res.value)

