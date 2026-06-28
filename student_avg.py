# Create class Student that takes three Marks and has a method called average 
class Student:
  def __init__(self , name , maths , english , science):
    self.name = name
    self.maths = maths
    self.english = english 
    self.science = science

  def calc_avg(self):
    average_marks = (self.maths + self.english + self.science) //3
    return average_marks
  
student1 = Student("XYZ", 89, 89, 88)
print(f"Student name = {student1.name}")
print(f"Student mark in maths = {student1.maths}")
print(f"Student mark in english = {student1.english}")
print(f"Student mark in science = {student1.science}")
print(f"{student1.name}'s overall percentage : {student1.calc_avg()}%")