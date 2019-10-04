from graphics import *
import stack

def InfixToPostfix(expr):
  pass

def EvaluatePostfix(s):
  while 2 < s.size():
    if s.off() == "+":
      left = s.off()
      right = s.off()
      s.on(left + right)
  return s.off()


def test_stack():
  s = stack.Stack()
  s.on(3)
  s.on(5)
  s.on("+")
  print(EvaluatePostfix(s))

def main():
  points = []
  LOWX = -10
  HIGHX = +10
  LOWY = -10
  HIGHY = +10
  INC_X = .1

  win = GraphWin("My calculator", 500, 500)
  win.setCoords(LOWX, LOWY, HIGHX, HIGHY)
  
  x = LOWX
  while x <= HIGHX:
    y = x ** 3
    points.append([x,y])
    x += INC_X

  for i in range(len(points)-1):
    # c = Circle(Point(points[i][0], points[i][1]), .1)
    # c.draw(win)
    l = Line(Point(points[i][0], points[i][1]), Point(points[i+1][0], points[i+1][1]))
    l.draw(win)

  win.getMouse()
  win.close()

if __name__ == "__main__":
  # main()
  test_stack()