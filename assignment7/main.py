from bst import BST, Node
from students import Student

def parseStudent(line):
  split_line = line.split()
  new_student = Student(split_line[0], split_line[1], split_line[2].strip(), split_line[3], split_line[4])
  return new_student

def main():
  bst = BST();
  lines = open("../data/InsertNames.txt").readlines()
  dups = 0
  for i in range(len(lines)):
    new_student = parseStudent(lines[i])
    if not bst.Insert(new_student):
      dups += 1
  print("%s duplicates while inserting." % dups)
  bst.Traverse(averageAge)
  global TOTAL_AGE
  print("average age of students", (TOTAL_AGE / bst.Size()))
  lines = open("../data/DeleteNames.txt").readlines()
  deleted = 0
  for i in range(len(lines)):
    dummy_student = Student("", "", lines[i].strip(), "", "")
    if bst.Delete(dummy_student):
      deleted += 1
  print("%s students deleted." % deleted)
  retrieved = 0
  retrievedTotalAge = 0
  lines = open("../data/RetrieveNames.txt").readlines()
  for i in range(len(lines)):
    dummy_student = Student("", "", lines[i].strip(), "", "")
    student = bst.Retrieve(dummy_student)
    if student is not None:
      retrieved += 1
      retrievedTotalAge += int(student.age)
  avg = (retrievedTotalAge / retrieved)
  print("%s students retrieved\naverage age of retrieved students %s" % (retrieved, avg))

TOTAL_AGE = 0
def averageAge(item):
  global TOTAL_AGE
  TOTAL_AGE += int(item.age)
  
if __name__ == "__main__":
  main()