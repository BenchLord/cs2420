import datetime

def bubbleSort(l):
  start = datetime.datetime.now()
  done = False
  passes = 0
  while not done:
    done = True
    left = len(l) - 1
    for i in range(left):
      # swap values if the second value is smaller
      if l[i] > l[i+1]:
        old = l[i]
        l[i] = l[i+1]
        l[i+1] = old
        done = False
    left -= 1
    passes += 1
  return passes, (datetime.datetime.now() - start).microseconds

def shakerSort(l):
  start = datetime.datetime.now()
  done = False
  passes = 0
  left = 0
  right = len(l) - 1
  while not done:
    done = True
    passes += 1
    # pass from left to right
    for i in range(left, right):
      if l[i] > l[i+1]:
        old = l[i]
        l[i] = l[i+1]
        l[i+1] = old
        done = False
    if done:
      break
    right -= 1
    passes += 1
    # pass from right to left
    for i in range(right, left, -1):
      if l[i] < l[i-1]:
        old = l[i]
        l[i] = l[i-1]
        l[i-1] = old
        done = False
    if done:
      break
    left += 1
  return passes, (datetime.datetime.now() - start).microseconds

def selectionSort(l):
  start = datetime.datetime.now()
  passes = 0
  for i in range(len(l) - 1):
    newIndex = i
    # find smallest out of remaining numbers
    for j in range(i+1, len(l)):
      if l[j] < l[newIndex]:
        newIndex = j
    # swap values if needed
    if newIndex != i:
      old = l[i]
      l[i] = l[newIndex]
      l[newIndex] = old
    passes += 1
  passes += 1
  return passes, (datetime.datetime.now() - start).microseconds

def mergeSort(l):
  pass

def quickSort(a, low, high, modified=False):
  # if modified than swap the middle index for the low index
  # for loop from low + 1 to high
  # swap smaller than pivot for leftmost bigger than pivot
  # swap pivot for rightmost smaller than pivot
  # recurse with values left of pivot & values right of pivot

  # base case is 1 or 0 items. if high - low <= 0
  if high - low <= 0:
    return
  if modified:
    mid = (low + high) // 2
    a[low],a[mid] = a[mid], a[low]
  pivot = low
  lmgt = low + 1
  for i in range(low+1, high+1):
    if a[i] < a[pivot]:
      a[i], a[lmgt] = a[lmgt], a[i]
      lmgt += 1
  pivot = lmgt - 1
  a[low], a[pivot] = a[pivot], a[low]
  quickSort(a, low, pivot - 1, modified)
  quickSort(a, pivot + 1, high, modified)