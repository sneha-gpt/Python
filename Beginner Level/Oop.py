# Task -> Create ATM Machine 

class ATM:

    def __init__(self):
        self.__pin = 0
        self.__balance = 0

        self.menu()

    def menu(self):
        print(""" Enter 1 to set pin
                  Enter 2 to check balance
                  Enter 3 to credit amount
                  Enter 4 to debit amount
                  Enter 5 to exit
              """)
        
        task = int(input("Enter task: "))

        match task:
            case 1:
                self.set_pin()
            case 2:
                self.check_balance()
            case 3:
                self.credit()
            case 4: 
                self.debit()
            case 5: 
                self.exit()
            case _:
                print("Wrong task")
    
    def check_pin(self):
        
        enter_pin = input("Enter pin: ")
        if enter_pin != self.__pin:
            print("Wrong pin!!")
            return False
        
        return True
        
    def set_pin(self):
        
        enter_pin = input("Enter pin: ")
        self.__pin = enter_pin
        print("Pin set successfully")

        self.menu()
    
    def check_balance(self):

        if self.check_pin():
            print(f"Balance: {self.__balance}")

        self.menu()

    def credit(self):

        if self.check_pin():
           amount = int(input("Enter amount: "))
           self.__balance = self.__balance + amount
           print("Amount credited successfully")

        self.menu()
       
    def debit(self):

        if self.check_pin():
           amount = int(input("Enter amount: "))
           
           if self.__balance >= amount:
               self.__balance = self.__balance - amount
               print("Amount debited successfully")
           else:
               print("Insufficient amount!!")
        self.menu()

    def exit(self):

        print("Thank you!!")

sbi = ATM()






