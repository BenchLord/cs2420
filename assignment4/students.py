import time

class Student:
  def __init__(self, fname, lname, ssn, email, age):
    self.fname = fname
    self.lname = lname
    self.ssn = ssn
    self.email = email
    self.age = age

def show_progress(percent, segments):
  symbol_count = int(percent // (100 // segments)) # symbol represents 5%
  symbols = ""
  if 0 < symbol_count:
    symbols = "="*(symbol_count - 1)
  if symbol_count < segments:
    last_symbol = ">"
    end_string = ""
  else:
    last_symbol = "="
    end_string = "\n"
  symbols += last_symbol + " "*(segments - len(symbols) - 1)
  print("\r%3d%% [%s]" % (percent, symbols), end="%s" % end_string)

def main():
  time_started = time.time()
  students = []
  duplicates = 0
  lines = open("../data/InsertNames.txt", "r").readlines()
  total_lines = len(lines)
  for i in range(total_lines):
    progress_percent = i * 100 / (total_lines - 1)
    show_progress(progress_percent, 10)
    split_line = lines[i].split()
    new_student = Student(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4])
    for student in students:
      if student.ssn == new_student.ssn:
        duplicates += 1
        print("Duplicate student: %s %s" % (new_student.fname, new_student.lname))
        continue
    students.append(new_student)
  time_elapsed = (time.time() - time_started)
  print("LINES:%13d\nDUPLICATES:%8d\nSECONDS: %10d" % (total_lines, duplicates, time_elapsed))
  

if __name__ == "__main__":
    main()