from graph import Graph

def main():
  fin = open("data.txt", "r")
  numVertices = int(fin.readline())
  g = Graph(numVertices)
  numEdges = int(fin.readline())
  for i in range(numEdges):
    edge = fin.readline().split(" ")
    v0 = int(edge[0])
    v1 = int(edge[1])
    g.addEdge(v0, v1)
  numTests = int(fin.readline())
  for i in range(numTests):
    vertices = fin.readline().split(" ")
    v0 = int(vertices[0])
    v1 = int(vertices[1])
    path = g.findPathDepth(v0, v1)
    print("Depth first: path between %d and %d: %s" % (v0, v1, path))
    path = g.findPathBreadth(v0, v1)
    print("Breadth first: path between %d and %d: %s" %(v0, v1, path))

if __name__ == "__main__":
  main()
