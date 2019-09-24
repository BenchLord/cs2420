import datetime

def bubbleSort(l):
  done = False
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
  return

def shakerSort(l):
  done = False
  left = 0
  right = len(l) - 1
  while not done:
    done = True
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
  return

def selectionSort(l):
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
  return

# measure swaps by
def mergeSort(l):
  if len(l) <= 1:
    return
  half = len(l) // 2
  left = l[:half]
  right = l[half:]
  mergeSort(left)
  mergeSort(right)
  for i in range(len(l)):
    if len(left) > 0 and len(right) > 0:
      if left[0] < right[0]:
        l[i] = left.pop(0)
      else:
        l[i] = right.pop(0)
    elif len(left) > 0:
      l[i] = left.pop(0)
    else:
      l[i] = right.pop(0)

def countingSort(l):
  # create new list with same length as l
  counts = [0]*len(l)
  for num in l:
    # increment counts at index num by 1 for
    # every instance of num in l
    counts[num] += 1
  insert = 0
  for i in range(len(counts)):
  # f[i] is how many times i appears in l
    count = counts[i]
    for j in range(count):
      l[insert] = i
      insert += 1

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
  for i in range(low, high+1):
    if a[i] < a[pivot]:
      a[i], a[lmgt] = a[lmgt], a[i]
      lmgt += 1
  pivot = lmgt - 1
  a[low], a[pivot] = a[pivot], a[low]
  quickSort(a, low, pivot - 1, modified)
  quickSort(a, pivot + 1, high, modified)