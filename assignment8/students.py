import time

class Student:
  def __init__(self, fname, lname, ssn, email, age):
    self.fname = fname
    self.lname = lname
    self.ssn = ssn
    self.email = email
    self.age = age
  def __eq__(self, rhs):
    return self.ssn == rhs.ssn
  def __lt__(self, rhs):
    return self.ssn < rhs.ssn
  def __le__(self, rhs):
    return self.ssn <= rhs.ssn
  def __gt__(self, rhs):
    return self.ssn > rhs.ssn
  def __ge__(self, rhs):
    return self.ssn >= rhs.ssn
  def __int__(self):
    return int(self.ssn.replace('-', ''))
    
