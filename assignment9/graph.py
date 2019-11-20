
class Graph:
  def __init__(self, numVertices):
    self.mVertices = [[False] * numVertices for i in range(numVertices)] 
    self.mNumVertices = numVertices

  def indexValid(self, v):
    return (0 <= v and v < self.mNumVertices)

  def addEdge(self, v0, v1): # returns False on bad edge
    if not (self.indexValid(v0) and self.indexValid(v1)):
      return False
    if self.isEdge(v0, v1) or v0 == v1:
      return False
    self.mVertices[v0][v1] = True
    return True

  def findPath(self, v0, v1):
    pass

  def getNeighbors(self, v):
    if not self.indexValid(v):
      return []
    neighbors = []
    for i in range(len(self.mVertices[v])):
      if self.mVertices[v][i]:
        neighbors.append(i)
    return neighbors

  def isEdge(self, v0, v1):
    if not (self.indexValid(v0) and self.indexValid(v1)):
      return False
    return self.mVertices[v0][v1]

