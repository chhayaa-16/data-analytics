# 6 august 
company_name = "ABC" 

def name() :
    print (company_name)


def calculate_salary(basic):
    hrs = basic * 0.98
    ot = basic + 1000
    Actual = basic + hrs + ot 
    return Actual


class Employee :

    def __init__ (self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary


    def show(self):
        print("the id of employee :",self.id)
        print("the name of employee :",self.name)
        print("the salary of employee :",self.salary)



if __name__ == "__main__":            # name variavle 
    print("this is testing code")