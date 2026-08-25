

# # student={
# #     "Chaya" :  82,
# #     "seema" : 67,
# #     "cp" : 87,
# #     "raj" : 34,
# #     "minal" : 22,
# #     "ritu" : 54

# # }


# # def info():

# #     for name ,marks in student.items():
# #         print(f"{name}:{marks}")



# # pas={ }

# # fail={ }



# # def result():

# #     for i,marks in student.items():

# #      if marks>35:
# #         print("pass")
    
# #      else:
# #         print("fail")

# # result()
        

# # def remark():
# #     for i,marks in student.items():

# #      if marks>35:

# #         pas[i]= marks 
# #         print(pas)
        
# #     else:

# #          fail[i]=marks
# #          print(fail)
# # remark()



# # def rank():
# #    count=len(student)

# #    student.sort(reverse=True)

# # while i <= count:

# #    for j in student.items():
# #       print(f"the rank of{j} is {i}")
      
   
# # rank()






# # stud={
     
# #     cp=[sci:23 ],
# #     chhaya=[54,67,87,45,98,],
# #     seema=[65,34,87,56,45],

# # }



# # def info():
# #     for name ,marks in stud.items():
# #        print(f"{name}:{marks}")




# # def result():

# #    for i,marks in stud.items():

# #      if marks>35:
# #        print("pass")
    
# #      else:
# #       print("fail")

# # result()
        

# # pas={ }

# # fail={ }



# # def remark():
# #     for i,marks in stud.items():

# #      if marks>35:

# #        pas[i]= marks 
# #        print(pas)
        
# #     else:

# #            fail[i]=marks
# #            print(fail)
# # remark()










# # # ------------------------ HOMEWORK EXAMPLE -------------------

# # student = {
# #     "A": 87,
# #     "B": 34,
# #     "C": 68,
# #     "D": 91,
# #     "E": 22,
# # }

# # pas= {}
# # fail= {}


# # def student_data():
# #     for name, marks in student.items():
# #         print(f"{name} : {marks}")


# # def result():
# #     for name, marks in student.items():
# #         if marks >= 35:
# #             print(f"{name} {marks} is Pass")
            
# #         else:
# #             print("Fail")

# # def pas():
# #     for name, marks in student.items():
# #         if marks >= 35:
# #             pas[name] = marks
# #             return pas
# #         else:
# #             fail[name] = marks
# #     return pas, fail

# # def pass_std():
# #     for name, marks in student.items():
# #         if marks >= 35:
# #             pass_student[name] = marks
# #         else:
# #             fail[name] = marks
# #     return pass_student, fail

# # def rank():
# #     count = len(student)
# #     student.sort(reverse = True)
    


    
#     marks_list = sorted(student.values(), reverse=True)
    
#     index = 0
#     count = len(marks_list)

#     while index < count:
#         current_mark = marks_list[index]
        
#         for name, marks in student.items():
#             if marks == current_mark:
#                 print(f"Rank {index + 1}: {name} : {marks}")
                
#         index += 1  

# student_data()
# result()
# print(pass_std())
# rank()



# students = {
#     "Student1": {
#         "python": 67,
#         "java": 82,
#         "cpp": 70,
#         "c language": 80,
#         "IT": 60
#     },

#     "Student2": {
#         "python": 92,
#         "java": 81,
#         "cpp": 84,
#         "c language": 33,
#         "IT": 80
#     },

#     "Student3": {
#         "python": 75,
#         "java": 69,
#         "cpp": 82,
#         "c language": 70,
#         "IT": 74
#     },

#     "Student4": {
#         "python": 80,
#         "java": 67,
#         "cpp": 20,
#         "c language": 80,
#         "IT": 45
#     },

#     "Student5": {
#         "python": 60,
#         "java": 72,
#         "cpp": 68,
#         "c language": 75,
#         "IT": 70
#     },

    
# # }

# # def student_data():
# #     for name, marks in students.items():
# #         print(f"{name} : {marks}")

# #     return students

# # def pas_fail():
# #     result = {}
# #     for name, marks in students.items():
# #         result[name]={}
# #         # print(name)
# #         for subject, marks in marks.items():
            
# #             if marks >= 35:
# #              #print(f"{name} {marks} is Pass")

# #              result[name][subject]="pass"
            
            
# #             else:
# #              #print("Fail")
# #              result[name][subject]="fail"
# #     print(result)

# #     return result


# # # student_data()
# # # pas_fail()




# # def ranking():
# #     sort_student = sorted(
# #        students.items(),
# #        key=lambda X:sum(X[1].values()),
# #        reverse=True)


# #     rank_info = {}
# #     rank = 1

# #     for name, mark in sort_student :
# #         total = sum(mark.values())
# #         rank_info[name]={
# #         "total":total,
# #         "rank":rank
# #         }
# #         rank +=1

# #     print(rank_info)



# ### 10-8-------------- oop concepts ------------------------------------------------------------------------------

# class bank:
#     def __init__(self,__balance):
#         self.__balance = __balance

#     def get_deposit(self,amount):
#         self.__balance += amount                              # get used only for a accept the value 
#                                                               # set used for update the value and print 
#         print(self.__balance)                                 # sinle underscore for protected
#                                                                 #double underscore for private

#     def set_withdraw(self,amount):
#         self.__balance -= amount

#         print(self.__balance)
        


# ob=bank(10000)
# print(f"the available balance is : {ob._bank__balance}")

# ob.get_deposit(500)
# print(f"the available  balance is: {ob._bank__balance}")                # bank - class name 

# ob.set_withdraw(2000)
# print(f"the available balance is: {ob._bank__balance}")

# # ==================================================================================================

# # class student:
# #     def __init__ (self):
# #         self.mark = 85

# # c=student()

# # print(c.mark)




# ======================11-8-26=============seaborn=====

import seaborn as sea
import matplotlib.pyplot as plt

data = sea.load_dataset("tips")
#print(data.head())

# print(data.head())

# sea.kdeplot(data["tip"])
# sea.displot(data["total_bill"])
# sea.histplot(data["total_bill"])



# titanic = sea.load_dataset("titanic")
# print(titanic.columns)

# # sea.histplot(titanic["total_bill"])
# plt.show()


# print(data["total_bill"].mean())
# # plt.title("total_bill")
# plt.figure(figsize=(5,10))

# # sea.pairplot(data = data , x_vars="total_bill")
# sea.histplot(data =data, x="total_bill")
# sea.set_style("whitegrid")
# # plt.show()

# sea.countplot(data = data , x="day", hue="sex")
# plt.show()

# sea.boxplot(data=data , x="day", y="total_bill", hue="sex")
# plt.show()


# sea.scatterplot(data = data, x="day", y="total_bill",hue="sex",size="size")
# plt.show()


# data = sea.load_dataset("flights")      # new data set 

# print(data)
# sea.lineplot(data=data,x="month",y="passengers",hue="year")

# plt.show()

corelation = data.select_dtypes("number").corr()
print(corelation)

sea.heatmap(corelation ,annot=True, cmap="coolwarm")                 #annot use for showing number in a box 
                                                                    #cmap use for change the colour
plt.show()