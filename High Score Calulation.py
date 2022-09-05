# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇




# We need to create a variable that is going to capture the exact variable by making the variable equal zero or multiplying whatever is applied to it by 1

# print(len(student_scores))

num_capture = 0

for student in student_scores:


    if student > num_capture:

        num_capture = student

print(f"The highest score in the class is {num_capture}")

        




   

    










# capture = 1

# for score in student_scores:

#     each_score = capture * score
#     print(each_score)






  





