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
  # test bubble sort
  randomList = createRandomList(10)
  expectedResult = sorted(randomList[:])
  passes, micros = sorting.bubbleSort(randomList)
  if Test("Bubble sort").assertEqual(randomList, expectedResult):
    printInfo(passes, micros)

  # test selection sort
  randomList = createRandomList(10)
  expectedResult = sorted(randomList[:])
  passes, micros = sorting.selectionSort(randomList)
  if Test("Selection sort").assertEqual(randomList, expectedResult):
    printInfo(passes, micros)

  # test shaker sort
  randomList = createRandomList(10)
  expectedResult = sorted(randomList[:])
  passes, micros = sorting.shakerSort(randomList)
  if Test("Shaker sort").assertEqual(randomList, expectedResult):
    printInfo(passes, micros)

if __name__ == "__main__":
  main()