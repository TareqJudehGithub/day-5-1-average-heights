# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_heights = 0
num_students = 0
for item in student_heights:
  total_heights += item
  num_students += 1

avg_std_height =  total_heights / num_students
print(f"Average students height: {round(avg_std_height)}")

# Solutoin #2:

avg_heights2 = sum(student_heights) / len(student_heights)
print(f"Average students height: {round(avg_heights2)}")




