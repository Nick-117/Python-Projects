student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇

for score in student_scores:
    # print(score)
    # print(student_scores[score])
    if student_scores[score] >= 91:
       student_scores[score] = "Outstanding"
        # print("Outstanding")
       student_grades[score] = str(student_scores[score])
    elif student_scores[score] in range(80, 90):
        student_scores[score] = "Exceeds Expectations"
        #  print("Exceeds Expectations") 
        student_grades[score] = str(student_scores[score])
    elif student_scores[score] in range(70, 80):
        student_scores[score] = "Acceptable"
        student_grades[score] = str(student_scores[score])
        #  print("Acceptable")

       
    elif student_scores[score] <= 70:
        student_scores[score] = "Fail"
        student_grades[score] = str(student_scores[score])
        # print("Fail")   






#Don't change the code below 👇
print(student_grades)





    

