from graph import Graph

def main():
  g = Graph(5)
  print("adding edge between vertex 0 and 4")
  g.addEdge(0, 4)
  for vertex in g.mVertices:
    print(vertex)
  print("trying to add edge between invalid vertices 10 and 20")
  ok = g.addEdge(10, 20)
  print(ok)

if __name__ == "__main__":
  main()
