import random
import sorting
import sys
import math

def createRandomList(size):
  l = []
  for i in range(size):
    l.append(random.randint(0, size - 1))
  return l

def createMostlySortedList(size):
  l = createRandomList(size)
  l.sort()
  l[0], l[size - 1] = l[size - 1], l[0]
  return l


def main():
  sys.setrecursionlimit(5000)
  sorts = [sorting.bubbleSort, sorting.selectionSort, sorting.shakerSort, sorting.countingSort, sorting.mergeSort, sorting.quickSortModified, sorting.quickSortHelper] # all sorting algorithms
  for sort in sorts:
    print("\t" + sort.__name__, end="")
  print()
  for log in range(3, 13):
    size = 2**log
    print(log, end="\t")
    for sort in sorts:
      a = createMostlySortedList(size)
      b = a[:]
      b.sort()
      counts = [0, 0] # [compares, swaps]
      sort(a, counts) # convert functions to take count and increment [compares, swaps]
      if a != b:
        print("ERROR: " + sort.__name__ + " did not sort values correctly")
      print(math.log(counts[1] + 1, 2), end="\t")
    print()

if __name__ == "__main__":
  main()
