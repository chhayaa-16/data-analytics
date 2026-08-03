# import input
# import matplotlib.pyplot as mp

# student=input.student_data()
# print(student)

# ranking = input.ranking()
# print(ranking)

# pas_fail=input.pas_fail()
# print(pas_fail)

# names=[]
# total= []

# for name,marks in student.items():
#     totals= sum(marks.values())

#     total.append(totals)
#     names.append(name)

# print(names)
# print(total)

# # mp.figure(figsize=(10,9))

# # mp.bar(names,total)
# # mp.title("nameVStotal")
# # mp.xlabel("student name")
# # mp.ylabel("marks")

# # mp.show()

# # pas=[23,45,2,54,8,89]               #  -----------------alternate option-----------
# # fai=[34,65,9,00,4]



# # pas=[]
# # fai=[]

# pas_student=0
# fail_student=0

# for name, subjects in pas_fail.items():

#     if "fail" in subjects.values():
#         fail_student += 1
#     else:
#         pas_student += 1




# mp.figure(figsize=(10,9))
# mp.title("student result")

# mp.pie(
#     [pas_student,fail_student],
#      labels=["Pass Student", "Fail Student"],
# )

# mp.show()


#------------------asignment questions--------------


# import chart_input
# import matplotlib.pyplot as mp



# user_data = chart_input.display()
# print(user_data)

# sus = chart_input.suspicious_users()
# print(sus)

# highest = chart_input.h_failed_attempt()
# print(highest)

# count = chart_input.normal_suspicious()
# print(count)


# names = []
# attempts = []

# for name, value in user_data.items():

#     names.append(name)
#     attempts.append(value)



# mp.figure(figsize=(8,4))

# mp.bar(names, attempts)

# mp.title("Failed Attempts")

# mp.xlabel("Users")

# mp.ylabel("Failed Attempts")

# mp.show()

# # mp.figure(figsize=(8,4))

# # mp.title("Normal vs Suspicious Users")

# # mp.show()