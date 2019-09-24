def bubbleSort(l, c):
  done = False
  while not done:
    done = True
    left = len(l) - 1
    for i in range(left):
      # swap values if the second value is smaller
      c[0] += 1
      if l[i] > l[i+1]:
        old = l[i]
        l[i] = l[i+1]
        l[i+1] = old
        c[1] += 1
        done = False
    left -= 1
  return

def shakerSort(l, c):
  done = False
  left = 0
  right = len(l) - 1
  while not done:
    done = True
    # pass from left to right
    for i in range(left, right):
      c[0] += 1
      if l[i] > l[i+1]:
        old = l[i]
        l[i] = l[i+1]
        l[i+1] = old
        c[1] += 1
        done = False
    if done:
      break
    right -= 1
    # pass from right to left
    for i in range(right, left, -1):
      c[0] += 1
      if l[i] < l[i-1]:
        old = l[i]
        l[i] = l[i-1]
        l[i-1] = old
        c[1] += 1
        done = False
    if done:
      break
    left += 1
  return

def selectionSort(l, c):
  for i in range(len(l) - 1):
    newIndex = i
    # find smallest out of remaining numbers
    for j in range(i+1, len(l)):
      c[0] += 1
      if l[j] < l[newIndex]:
        newIndex = j
    # swap values if needed
    if newIndex != i:
      old = l[i]
      l[i] = l[newIndex]
      l[newIndex] = old
      c[1] += 1
  return

# measure swaps by
def mergeSort(l, c):
  if len(l) <= 1:
    return
  half = len(l) // 2
  left = l[:half]
  right = l[half:]
  mergeSort(left, c)
  mergeSort(right, c)
  for i in range(len(l)):
    if len(left) > 0 and len(right) > 0:
      c[0] += 1
      if left[0] < right[0]:
        c[1] += 1
        l[i] = left.pop(0)
      else:
        c[1] += 1
        l[i] = right.pop(0)
    elif len(left) > 0:
      c[1] += 1
      l[i] = left.pop(0)
    else:
      c[1] += 1
      l[i] = right.pop(0)

def countingSort(l, c):
  # create new list with same length as l
  counts = [0]*len(l)
  for num in l:
    # increment counts at index num by 1 for
    # every instance of num in l
    c[0] += 1
    counts[num] += 1
  insert = 0
  for i in range(len(counts)):
  # counts[i] is how many times i appears in l
    count = counts[i]
    for j in range(count):
      l[insert] = i
      c[1] += 1
      insert += 1

def quickSort(a, c, low, high, modified):
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
    c[0] += 1
    if a[i] < a[pivot]:
      a[i], a[lmgt] = a[lmgt], a[i]
      c[1] += 1
      lmgt += 1
  pivot = lmgt - 1
  a[low], a[pivot] = a[pivot], a[low]
  c[1] += 1
  quickSort(a, c, low, pivot - 1, modified)
  quickSort(a, c, pivot + 1, high, modified)

def quickSortModified(a, c):
  quickSort(a, c, 0, len(a) - 1, True)

def quickSortHelper(a, c):
  quickSort(a, c, 0, len(a) - 1, False)