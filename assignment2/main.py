import random
import sorting
import sys
import math

def createRandomList(size):
  l = []
  for i in range(size):
    l.append(random.randint(0, size - 1))
  return l

def assignment2():
  l = createRandomList(10)
  l1 = l[:]
  l2 = l[:]
  l3 = l[:]
  l4 = l[:]
  ls = sorted(l)
  sorting.quickSort(l1, 0, len(l1) - 1)
  sorting.quickSort(l2, 0, len(l2) - 1, True)
  sorting.mergeSort(l3)
  sorting.countingSort(l4)
  print("Unsorted: ", l)
  print("Epected: ", ls)
  print("After quick: ", l1)
  print("After modified quick: ", l2)
  print("after merge: ", l3)
  print("after counting: ", l4)

def main():
  sys.setrecursionlimit(5000)
  sorts = [sorting.bubbleSort, sorting.selectionSort] # all sorting algorithms
  for sort in sorts:
    print("\t" + sort.__name__, end="")
  print()
  for log in range(3, 13):
    size = 2**log
    print(log, end="\t")
    for sort in sorts:
      a = createRandomList(size)
      b = a[:]
      b.sort()
      counts = [0, 0]
      sort(a, counts) # convert functions to take count and increment [compares, swaps]
      if a != b:
        print("ERROR: " + sort.__name__ + " did not sort values correctly")
      print(math.log(counts[1] + 1, 2), end="\t")
    print()

if __name__ == "__main__":
  # main()
  assignment2()
