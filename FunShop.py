# It is a console program "FunShop" with excess code
import operator
import re

print("-------- Welcome In Our Fun Shopping ---------------")
print("Note: Just for kidding.")

class Shop:

    def amount(self):
        amount_input = int(input("Enter your amount (Trillion Bitcoin): "))
        if amount_input == 97:
            print("You are successful.")
        elif amount_input > 97:
            amount_input = amount_input - 97
            print("You are successful.\nYou have paied ",amount_input,"Trillion Bitcoin excess\n"
                                                 "It will save for your next product when you will buy.\n")
        elif amount_input < 97:
            amount_input = 97 - amount_input
            print("You have paied ", amount_input, "Trillion Bitcoin Less. "
                                                   "Please don't due here. So Try Again dear.\n")
            self.amount()
        else:
            print("Doesn't match with your amount.\n")
            self.amount()

    def buy_product(self):
        print("Pay your bill with mastercard."
              "visa, american express,"
              "dutch bangla, paypal.")
        try:
            bill = int(input("\n\t\t\tPress 1 if you wanna go to menu.\n"
                             "For buy give here your card number (8 digit): "))
            if len(str(bill)) == 8:
                self.amount()
            elif bill == 1:
                self.category()
            else:
                print("Must have need 8 digit number.\n")
                self.buy_product()

        except ValueError:
            print("Wrong pressed, Try agaon.\n")
            self.buy_product()

    def super_computer(self):

        print("\n***supercomputer***\n\t\t\tDescription: A supercomputer is a computer that performs at or near the"
              " currently highest\n"
              "operational rate for computers.  Traditionally, supercomputers have been used for scientific and \n"
              "engineering applications that must handle very large databases or do a great amount of computation\n"
              "(or both). Although advances like multi-core processors and GPGPUs (general-purpose graphics "
              "processing\n"
              "units) have enabled powerful machines for personal use (see: desktop supercomputer,"
              "\nGPU supercomputer),"
              "by definition, a supercomputer is exceptional in terms of performance.\n\n"
              "\t\t\tPrice: 97 Quintillion Bitcoin(BTC)\n"
              "Price is very low.\n")
        choice_in = input("\n1. Buy this product\n"
                          "2. Go to menu\n"
                          "Press number(1~2): ")
        if choice_in == '1':
            self.buy_product()
        elif choice_in == '2':
            self.category()
        else:
            print("Wrong pressed. Try.")

    def aircraft(self):
        print("Details")
        self.category()

    def pen(self):
        print("Details")
        self.category()

    def gmail_method(self):
        pattern = r"@gmail.com"
        self.gmail =  input("Enter Your Gmail: ")
        if re.search(pattern, self.gmail):
            self.email = self.gmail
            #print(self.email)
        else:
            print("Your gmail wrong. (@gmail.com)\nTry again.\n")
            self.gmail_method()

    def password(self):
        self.__password_1 = input("Enter Your Password: ")
        self.__password_2 = input("Enter confirm Password: ")
        if operator.eq(self.__password_1, self.__password_2):
            print("Your account has been created. Thanks.")
            self.signin()
        else:
            print("Your password dosent match, Try again.\n")
            self.password()

    def registration(self):
        print("\n\n**************Registration************\n")
        self.fullname = input("Enter your fullname: ")
        self.gmail_method()
        #self.gmail = input("Enter your gmail: ")
        self.password()

    def signin(self):
        print("************SignIn**********\n")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        if email == self.email:
            if password == self.__password_1:
                print("You are singed in. Thnaks.\n")
                return self.category()
            else:
                print("password doesn't matching\nTry again")
                self.signin()
        else:
            print("Email doesn't matching\nTry again")
            self.signin()

    def category(self):
        choose = input("\nYour choice:\n"
                       "\n1. Super Computer\n"
                       "2. Aircraft\n"
                       "3. Pen\n"
                       "\npress a number which product you want to get: ")
        if choose == '1':
            self.super_computer()
        elif choose == '2':
            return self.aircraft()
        elif choose == '3':
            return self.pen()
        else:
            print("\nWrong Pressed.\nAgain")
            self.category()

shop_obj = Shop()
shop_obj.registration()
# shop_obj.buy_product()
