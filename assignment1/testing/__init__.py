class Test:
  def __init__(self, name):
    self.name = name
    return
  def assertEqual(self, got, wanted):
    if got == wanted:
      print(self.name + ": \033[32m" + "SUCCESS\033[0m")
      return True
    print(self.name + ": \033[31m" + "FAILURE")
    print("  GOT: ", end='')
    print(got)
    print("  WANTED:", end='')
    print(wanted, end='')
    print("\033[0m"),
    return False