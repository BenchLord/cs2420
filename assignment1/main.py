import random
import sorting
from testing import Test
import datetime

def createRandomList(size):
  l = []
  for i in range(size):
    l.append(random.randint(0, size))
  return l

def printInfo(passes, micros):
  print(" %d passes in %dμs" % (passes, micros))

def main():
  randomList = createRandomList(10)
  randomList2 = randomList[:]
  randomList3 = randomList[:]
  randomList4 = randomList[:]
  randomList5 = randomList[:]
  expectedResult = sorted(randomList[:])

  print("Generated list: ", randomList)
  print("Expected result: ", expectedResult)
  sorting.bubbleSort(randomList)
  print("After Bubble sort: ", randomList)
  sorting.selectionSort(randomList2)
  print("After selection sort: ", randomList2)
  sorting.shakerSort(randomList3)
  print("After shaker sort: ", randomList3)

  sorting.mergeSort(randomList4)
  print("After merge sort: ", randomList4)

  sorting.quickSort(randomList5, 0, len(randomList5) - 1)
  print("After quick sort: ", randomList5)

if __name__ == "__main__":
  main()
