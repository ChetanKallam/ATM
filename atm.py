class Atm:
    def _init_(self,cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    
    def CashWithdrawl(self, amount):
        new_amount=50000-amount
        print("you have withdrawn the amount "+str(amount)+". Your remaining balance is"+str(new_amount))
    
    def BalanceEnquiry(self):
        print("your balance is 50000")
        
def main():
    Card_number = input("insert your card number:- ") 
    pin_number = input("enter your pin number:- ") 
    new_user = Atm(Card_number ,pin_number) 
    print("Choose your activity ") 
    print("1.Balance Enquriy 2.withdrawl") 
    activity = int(input("enter activity number :- "))
    if (activity==1):
        new_user.BalanceEnquiry()
    elif (activity==2):
        amount=int(input("enter amount to be withdrawn"))
        new_user.CashWithdrawl()
    else:
        print ("enter valid number")

if __name__=="__main__":
    main()