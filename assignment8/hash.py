import math

def isPrime(x):
  if x == 2:
    return True
  if x % 2 == 0:
    return False
  s = int(math.sqrt(x))
  for i in range(3, s+1, 2):
    if x % i == 0:
      return False
  return True
 
class Hash:
  def __init__(self, expected_size):
    size = expected_size * 2 + 1
    while not isPrime(size):
      size += 1
    self.mTable = [None] * size
    print("done")
    
  def Exists(self, item):
    key = int(item)
    index = key % len(self.mTable)
    while True:
      if self.mTable[index] is None:
        return False
      if self.mTable[index] and self.mTable[index] == item:
        return True
      index += 1
      if index >= len(self.mTable):
        index = 0

  def Traverse(self, callback):
    for i in range(len(self.mTable)):
      current = self.mTable[i]
      if current:
        callback(current)

  def Insert(self, item):
    key = int(item)
    index = key % len(self.mTable)
    if self.Exists(item):
      return False
    while True:
      if not self.mTable[index]:
        self.mTable[index] = item
        return True
      index += 1
      if index >= len(self.mTable):
        index = 0
  
  def Delete(self, item):
    key = int(item)
    index = key % len(self.mTable)
    while True:
      current = self.mTable[index]
      if current is None:
        return False
      if current and current == item:
        self.mTable[index] = False
        return True
      index += 1
      if index >= len(self.mTable):
        index = 0

  def Retrieve(self, item):
    if not self.Exists(item):
      return None
    key = int(item)
    index = key % len(self.mTable)
    while True:
      current = self.mTable[index]
      if current and current == item:
        return current
      index += 1
      if index >= len(self.mTable):
        index = 0

  def Size(self):
    size = 0
    for i in range(len(self.mTable)):
      if not self.mTable[i]:
        size += 1
    return size
