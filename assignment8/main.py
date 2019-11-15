from hash import Hash
from students import Student
import time

def parseStudent(line):
  split_line = line.split()
  new_student = Student(split_line[0], split_line[1], split_line[2].strip(), split_line[3], split_line[4])
  return new_student

def main():
  lines = open("../data/InsertNamesMedium.txt").readlines()
  hashtable = Hash(len(lines))
  time_started = time.time()
  dups = 0
  for i in range(len(lines)):
    new_student = parseStudent(lines[i])
    if not hashtable.Insert(new_student):
      dups += 1
  time_elapsed = time.time() - time_started
  print("%s duplicates while inserting." % dups)
  print("%s seconds\n" % time_elapsed)

  time_started = time.time()
  hashtable.Traverse(averageAge)
  global TOTAL_AGE
  time_elapsed = time.time() - time_started
  print("average age of students", (TOTAL_AGE / hashtable.Size()))
  print("%s seconds\n" % time_elapsed)

  lines = open("../data/DeleteNamesMedium.txt").readlines()
  time_started = time.time()
  deleted = 0
  failed = 0
  for i in range(len(lines)):
    dummy_student = Student("", "", lines[i].strip(), "", "")
    if hashtable.Delete(dummy_student):
      deleted += 1
    else:
      failed += 1
  time_elapsed = time.time() - time_started
  print("%s students deleted." % deleted)
  print("%s errors" % failed)
  print("%s seconds\n" % time_elapsed)

  retrieved = 0
  retrievedTotalAge = 0
  lines = open("../data/RetrieveNamesMedium.txt").readlines()
  time_started = time.time()
  failed = 0
  for i in range(len(lines)):
    dummy_student = Student("", "", lines[i].strip(), "", "")
    student = hashtable.Retrieve(dummy_student)
    if student is not None:
      retrieved += 1
      retrievedTotalAge += int(student.age)
    else:
      failed += 1
  avg = (retrievedTotalAge / retrieved)
  time_elapsed = time.time() - time_started
  print("%s students retrieved\naverage age of retrieved students %s" % (retrieved, avg))
  print("%s errors" % failed)
  print("%s seconds\n" % time_elapsed)

TOTAL_AGE = 0
def averageAge(item):
  global TOTAL_AGE
  TOTAL_AGE += int(item.age)
  
if __name__ == "__main__":
  main()
