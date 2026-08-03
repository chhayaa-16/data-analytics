

#----------------ATM WITHDRAWL----------------------------


    

def balance(self,balance,):
        self.balance=balance

        current_balance=40000
        User_amount=input("Enter amount:",User_amount)

        
        if(current_balance<=self.balance):
          input(" ready to withraw:")

        else:
            ("enter another value")


def withdraw(self,amount):
            
         if (amount<=self.balance):
             print("withdraw")
         else:
             print("invalid")

v1=atm(1234,20000)
v1.pin()
v1.balance()

