students=[]
succeed=[]
fail=[]
S1=int(input("Input marks for Student 1 :  "))
students.append(S1)
S2=int(input("Input marks for Student 2 :  "))
students.append(S2)
S3=int(input("Input marks for Student 3 :  "))
students.append(S3)
S4=int(input("Input marks for Student 4 :  "))
students.append(S4)
S5=int(input("Input marks for Student 5 :  "))
students.append(S5)
S6=int(input("Input marks for Student 6 :  "))
students.append(S6)
S7=int(input("Input marks for Student 7 :  "))
students.append(S7)
S8=int(input("Input marks for Student 8 :  "))
students.append(S8)
S9=int(input("Input marks for Student 9 :  "))
students.append(S9)
S10=int(input("Input marks for Student 10 :  "))
students.append(S10)
print(students)
students = [23, 45, 56, 67, 78, 90, 87, 55, 43, 32]

for marks in students:
    if marks >50:
        succeed.append(marks)
    else:
        fail.append(marks)

sum_failed=0
for i in fail:
    sum_failed+=i

AVG1=sum_failed/len(fail)
print(AVG1)

sum_passed=0
for i in succeed:
    sum_passed+=i

AVG2=sum_passed/len(succeed)
print(AVG2)

print(sum_passed)
print(sum_failed)

print(fail)
print(succeed)
list_which_failed=len(fail)
list_which_succeeded=len(succeed)
print(list_which_failed)
print(list_which_succeeded)

