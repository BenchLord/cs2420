import datetime

def bubbleSort(l):
  start = datetime.datetime.now()
  done = False
  passes = 0
  while not done:
    done = True
    for i in range(len(l) - 1):
      # swap values if the second value is smaller
      if l[i] > l[i+1]:
        old = l[i]
        l[i] = l[i+1]
        l[i+1] = old
        done = False
    passes += 1
  return passes, (datetime.datetime.now() - start).microseconds

def shakerSort(l):
  # IMPLEMENT LOGIC
  return passes

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