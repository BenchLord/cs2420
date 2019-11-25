class Stack:
  def __init__(self):
    self.mStack = []
  def push(self, value):
    self.mStack.append(value)
  def pop(self):
    return self.mStack.pop()
  def isEmpty(self):
    return len(self.mStack) < 1
  def size(self):
    return len(self.mStack)
  def top(self):
    if self.isEmpty():
      return ""
    return self.mStack[-1]
