from graphics import *
import stack

def InfixToPostfix(infix):
  postfix = ""
  s = stack.Stack()
  for c in infix:
    if c in "0123456789xX":
      postfix += c
    elif c in "+-":
      while not s.isEmpty():
        if s.top() == "(":
          break
        postfix += s.pop()
      s.push(c)
    elif c in "*/":
      while not s.isEmpty():
        if not s.top() in "*/":
          break
        postfix += s.pop()
      s.push(c)
    elif c == "(":
      s.push(c)
    elif c == ")":
      while not s.isEmpty():
        ch = s.pop()
        if ch == "(":
          break
        postfix += ch
  while not s.isEmpty():
    postfix += s.pop()
  return postfix

def EvaluatePostfix(postfix, x):
  s = stack.Stack()
  result = 0
  for c in postfix:
    if c in "0123456789":
      s.push(float(int(c)))
    elif c in "xX":
      s.push(x)
    elif c == "*":
      rhs = s.pop()
      lhs = s.pop()
      s.push(lhs * rhs)
    elif c == "/":
      rhs = s.pop()
      lhs = s.pop()
      s.push(lhs / rhs)
    elif c == "+":
      rhs = s.pop()
      lhs = s.pop()
      s.push(lhs + rhs)
    elif c == "-":
      rhs = s.pop()
      lhs = s.pop()
      s.push(lhs - rhs)
  return s.pop()

def getPoints(expression, low, high, inc):
  points = []
  x = low
  while x <= high:
    y = EvaluatePostfix(expression, x)
    points.append([x, y])
    x += inc
  return points

def drawGraph(window, expression, points, number):
  colors = ["blue", "green", "red", "orange", "purple", "pink"]
  currentColor = colors[number % len(colors)]
  for i in range(len(points)-1):
    l = Line(Point(points[i][0], points[i][1]), Point(points[i+1][0], points[i+1][1]))
    l.setFill(currentColor)
    l.draw(window)
    yPos = 10 - number
    t = Text(Point(-8, yPos), expression)
    t.setFill(currentColor)
    t.setSize(15)
    t.draw(window)

def loop():
  LOWX = -10
  HIGHX = +10
  LOWY = -10
  HIGHY = +10
  INC_X = .1
  win = GraphWin("My calculator", 500, 500)
  win.setCoords(LOWX, LOWY, HIGHX, HIGHY)

  Line(Point(LOWX, 0), Point(HIGHX, 0)).draw(win)
  Line(Point(0, LOWY), Point(0, HIGHY)).draw(win)

  print("Thank you for using super calcutron 3000!")
  formulaCount = 0
  while True:
    choice = input("> ")
    if choice in ["q", "quit", "exit"]:
      break
    if choice in ["h", "help"]:
      print("input a formula or type quit to exit")
      continue
    postfix = InfixToPostfix(choice)
    points = getPoints(postfix, LOWX, HIGHX, INC_X)
    formulaCount += 1
    drawGraph(win, choice, points, formulaCount)

  win.close()

if __name__ == "__main__":
  loop()