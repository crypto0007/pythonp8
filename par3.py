class BankAccount:
    interest_rate=7;
    def set(self):
        self.acno=input("Enter Account no:");
        self.name=input("Enter name:");
        self.balance=int(input("Enter Balance:"));

    def deposite(self):
        self.deposite=int(input("Enter amount u want to deposite:"));
        self.balance=self.balance + self.deposite;
        print("Balance is: ",self.balance);
    def withdraw(self):
        self.deposite=int(input("Enter amount u want to deposite:"));
        self.balance=self.balance - self.deposite;
        print("Balance is: ",self.balance);

    def calc_interest(self):
        self.n=int(input("Enter  no of years for interest:"));
        self.interest=self.balance*BankAccount.interest_rate*self.n/100;
        print("Interest is: ",self.interest);
        
    def show(self):
        print("Account no: ",self.acno);
        print("Name: ",self.name);
        print("Balance: ",self.balance);

    def menu(self):
        while(1):
            print('1.set the values \n 2.Deposite \n 3.Withdraw \n 4. calculate interest \n 5.show details \n 6.exit');
            self.c=int(input("Enter ur choice:"));
            if(self.c==1):
                self.set();
            elif(self.c==2):
                self.deposite();
            elif(self.c==3):
                self.withdraw();
            elif(self.c==4):
                self.calc_interest();
            elif(self.c==5):
                self.show();
            else:
                break;
    
acc=BankAccount();
acc.menu();
