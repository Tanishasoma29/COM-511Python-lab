'''Experiment6: Write a program to create a list of student’s
records and search a student record using a dictionary.
CODE:'''
class Student:
 def GetStudent(self):
 self.rollno=input("Enter roll number:")
 self.name=input("Enter name:")
 self.physicsMarks=int(input("Enter Physics Marks:"))
 self.chemistryMarks=int(input("Enter Chemistry Marks:"))
 self.mathsMarks=int(input("Enter Maths Marks:"))
 return(self.rollno)
 def PutStudent(self):

print(self.rollno,self.name,((self.physicsMarks+self.chemistryMarks+sel
f.mathsMarks)/3))
 def Search(self,min,max):
 per=(self.physicsMarks+self.chemistryMarks+self.mathsMarks)/3
 if(per>=min and per<=max):
 return True
 else:
 return False
 studentDict=dict()
n=int(input("How many students you want to input:"))
for i in range(n):
 S=Student()
 rollno=S.GetStudent()
 studentDict.setdefault(rollno,S)
#SEARCHING FOR STUDENT RECORDS WITH ROLL NUMBERS
PEOVIDED BY THE USER
rollno=input("enter the roll number you want to search?:")
S=studentDict.get(rollno,"Not Found!")
if(isinstance(S,Student)):
 S.PutStudent()
else:
 print(S)
#PRINTNG RECORDS OF ALL USERS WITH MARKS GREATER
THAN 60%
print("All students who scored more than 60% are:")
min=int(input('Enter avg min value'))
max=int(input('Enter avg max value'))
gradeAStudent=list(filter(lambda
s:s.Search(min,max),studentDict.values()))
if(len(gradeAStudent)==0):
print("Record Not Found!")
else:
 for S in gradeAStudent:
 S.PutStudent()
