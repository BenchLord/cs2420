class Node:
  def __init__(self, item):
    self.mItem = item
    self.mLeft = None
    self.mRight = None

class BST:
  def __init__(self):
    self.mSize = 0
    self.mRoot = None

  def Exists(self, item):
    return self.existsR(item, self.mRoot)
  def existsR(self, item, current):
    if current is None:
      return False
    elif item == current.mItem:
      return True
    elif item < current.mItem:
      return self.existsR(item, current.mLeft)
    else:
      return self.existsR(item, current.mRight)

  def Insert(self, item):
    if self.Exists(item):
      return False
    n = Node(item)
    self.mRoot = self.insertR(n, self.mRoot)
    self.mSize += 1
    return True
  def insertR(self, n, current):
    if current is None:
      current = n
    elif n.mItem < current.mItem:
      current.mLeft = self.insertR(n, current.mLeft)
    else:
      current.mRight = self.insertR(n, current.mRight)
    return current

  def Traverse(self, callback):
    self.traverseR(self.mRoot, callback)
  def traverseR(self, current, callback):
    if current is None:
      return
    self.traverseR(current.mLeft, callback)
    callback(current.mItem)
    self.traverseR(current.mRight, callback)
    
  def Delete(self, item):
    if not self.Exists(item):
      return False
    self.mRoot = self.deleteR(item, self.mRoot)
    self.mSize -= 1
    return True
  def deleteR(self, item, current):
    if item < current.mItem:
      current.mLeft = self.deleteR(item, current.mLeft)
    elif item > current.mItem:
      current.mRight = self.deleteR(item, current.mRight)
    else:
      if current.mRight is None and current.mLeft is None:
        current = None
      elif current.mRight is None and current.mLeft is not None:
        current = current.mLeft
      elif current.mLeft is None:
        current = current.mRight
      else:
        heir = current.mRight
        while heir.mLeft is not None:
          heir = heir.mLeft
        current.mItem = heir.mItem
        current.mRight = self.deleteR(heir.mItem, current.mRight)
    return current
        
  def Retrieve(self, item):
    student = self.retrieveR(item, self.mRoot)
    return student
  def retrieveR(self, item, current):
    if current is None:
      return None
    if current.mItem == item:
      return current.mItem
    else:
      if item < current.mItem:
        return self.retrieveR(item, current.mLeft)
      else:
        return self.retrieveR(item, current.mRight)

  def Size(self):
    return self.mSize