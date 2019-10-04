class Stack:
  def __init__(self):
    self.mStack = []
  def on(self, value):
    self.mStack.append(value)
  def off(self):
    return self.mStack.pop()
  def empty(self):
    return len(self.mStack) < 1
  def size(self):
    return len(self.mStack)