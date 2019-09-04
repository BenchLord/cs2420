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