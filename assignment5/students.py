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

def insertStudents(students):
  time_started = time.time()
  duplicates = []
  lines = open("../data/InsertNames.txt", "r").readlines()
  total_lines = len(lines)
  print("Inserting students")
  for i in range(total_lines):
    progress_percent = i * 100 / (total_lines - 1)
    show_progress(progress_percent, 10)
    split_line = lines[i].split()
    new_student = Student(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4])
    for student in students:
      if student.ssn == new_student.ssn:
        duplicates.append(new_student)
        continue
    students.append(new_student)
  time_elapsed = (time.time() - time_started)
  print("LINES:%11d\nSECONDS: %8d\nDUPLICATES:" % (total_lines, time_elapsed))
  for student in duplicates:
    print(" %s %s" % (student.fname, student.lname))

def averageAge(students):
  average_age = 0
  total_students = len(students)
  time_started = time.time()
  print("Getting average age")
  for i in range(total_students):
    average_age += int(students[i].age)
    progress_percent = i * 100 / (total_students - 1)
    show_progress(progress_percent, 10)
  average_age /= total_students
  time_elapsed = (time.time() - time_started)
  print("STUDENTS:%8d\nAVERAGE:%9.4f\nSECONDS:%9d" % (total_students, average_age, time_elapsed))
    
def deleteStudent(students):
  time_started = time.time()
  lines = open("../data/DeleteNames.txt", "r").readlines()
  deleted = 0
  not_matched = []
  print("Deleting students")
  for i in range(len(lines)):
    progress_percent = i * 100 / (len(lines) - 1)
    show_progress(progress_percent, 10)
    ssn = lines[i][:-1]
    match = False
    index = 0
    while index < len(students):
      if students[index].ssn == ssn:
        students.pop(index)
        deleted += 1
        match = True
        break
      else:
        index += 1
    if not match:
      not_matched.append(ssn)
  time_elapsed = (time.time() - time_started)
  print("DELETED:%9d\nSECONDS:%9d\nDOES NOT EXIST:" % (deleted, time_elapsed))
  for ssn in not_matched:
    print(" %s" % ssn)

def retrieveStudent(students):
  time_started = time.time()
  lines = open("../data/RetrieveNames.txt", "r").readlines()
  average = 0
  retrieved = 0
  not_matched = []
  print("Retrieving students")
  for i in range(len(lines)):
    progress_percent = i * 100 / (len(lines) - 1)
    show_progress(progress_percent, 10)
    ssn = lines[i][:-1]
    match = False
    for student in students:
      if student.ssn == ssn:
        match = True
        retrieved += 1
        average += int(student.age)
        break
    if not match:
      not_matched.append(ssn)
  average = average / retrieved 
  time_elapsed = (time.time() - time_started)
  print("RETRIEVED:%7d\nAVERAGE:%9.4f\nSECONDS:%9d\nDOES NOT EXIST:" % (retrieved, average, time_elapsed))
  for ssn in not_matched:
    print(" %s" % ssn)

def main():
  students = []
  insertStudents(students)
  print()
  averageAge(students)
  print()
  deleteStudent(students)
  print()
  retrieveStudent(students)
  print()
  
if __name__ == "__main__":
  main()