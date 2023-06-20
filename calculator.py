class Calculator():
    def __init__(self):
        self.income_dict = {}
        self.expense_dict = {
            "tax": 0,
            "insurance": 0,
            "utilities": 0,
            "hoa": 0,
            "snow": 0,
            "vacancy": 0,
            "repairs": 0,
            "capex": 0,
            "property management": 0,
            "mortgage": 0
        }
        self.total_income = 0
        self.total_expense = 0
        self.cashflow = 0
        self.roi_dict = {
            "down payment": 0,
            "closing costs": 0,
            "rehab budget": 0
        }
        self.total_investment = 0
        self.annual_cash_flow = 0
        self.final_roi = 0.0
        



    def income(self):

        while True:

            response = input("What would you like to do? Add income, change existing income, show income, delete income or quit. ")
            if response.lower() == "add income":
                response = input("What type of income would you like to add? ")
                response2 = int(input("How much do you make from it? "))
                self.income_dict[response] = response2

            elif response.lower() == "change existing income":
                response = input("What income would you like to change? ")
                for key, value in self.income_dict.items():
                    if response.lower() == key:
                        response2 = int(input("What is the new income payment? "))
                        self.income_dict[response.lower()] = response2
                        break
            elif response.lower() == "delete income":
                response = input("What income would you like to change? ")
                for key, value in self.income_dict.items():
                    if response.lower() == key:
                        del self.income_dict[response.lower()]
                        break
            elif response.lower() == "quit":
                self.total_income = 0
                for key, value in self.income_dict.items():
                    self.total_income += value
                print(f"Your total income is {self.total_income}")
                print("Thank you.")
                break

            elif response.lower() == "show income":
                for key, value in self.income_dict.items():
                    print(f"{key} - {value}")

            else:
                print("Not a valid response, try again.")
    
    def expenses(self):
        while True:

            print("Total expenses listed down below:")
            for key, value in self.expense_dict.items():
                print(key, "-", value)
            
            response = input("What would you like to do? Change value, remove value, or quit. ")

            if response.lower() == "change value":
                response = input("What value would you like to change? ")
                for key, value in self.expense_dict.items():
                    if response.lower() == key:
                        response2 = int(input("What would you like to change the value to? "))
                        self.expense_dict[response] = response2
            
            elif response.lower() == "remove value":
                response = input("What value would you like to remove? ")
                for key, value in self.expense_dict.items():
                    if response.lower() == key:
                        self.expense_dict[response] = 0

            elif response.lower() == "quit":
                self.total_expense = 0
                for key, value in self.expense_dict.items():
                    self.total_expense += value
                print(f"Your total expenses is {self.total_expense}")
                print("Thank you.")
                break

            else:
                print("Not a valid response, try again.")

    
    def cash_flow(self):
        if self.income_dict and self.expense_dict:
            self.total_income = 0
            self.total_expense = 0
            for value in self.income_dict.values():
                self.total_income += value
            
            for value in self.expense_dict.values():
                self.total_expense += value
            
            print(f"Your total income is {self.total_income} and your total expense is {self.total_expense}")
            self.cashflow = self.total_income - self.total_expense
            print(f"Your total monthly cashflow is {self.cashflow}")

    def roi(self):

        while True:
            for key, value in self.roi_dict.items():
                    print(key, "-", value)
            
            response = input("What would you like to do? Change value, add value, remove value, find investment, find cash flow, find roi, or quit. ")

            if response.lower() == "change value":
                response = input("What value would you like to change? ")
                for key, value in self.roi_dict.items():  
                    if response.lower() == key:
                        response2 = int(input("What would you like to change the value to? "))
                        self.roi_dict[response] = response2

            elif response.lower() == "add value":
                response = input("What would you like to add? ")
                response2 = int(input("What is the the new value? "))
                self.roi_dict[response] = response2

            elif response.lower() == "remove value":
                response = input("What would you like to remove? ")
                del self.roi_dict[response]
            
            elif response.lower() == "find investment":
                self.total_investment = 0
                for key, value in self.roi_dict.items():
                    self.total_investment += value
                print(f"Your total investment is {self.total_investment}")
            
            elif response.lower() == "find cash flow":
                if self.cashflow:
                    self.annual_cash_flow = self.cashflow * 12
                    print(f"Your annual cash flow is {self.annual_cash_flow}")
                else:
                    print("Please find your cash flow first.")

            elif response.lower() == "roi":
                if self.annual_cash_flow and self.total_investment:
                    self.final_roi = (float(self.annual_cash_flow / self.total_investment))*100
                    print(f"You're roi finally comes out to {self.final_roi}%")

            elif response.lower() == "quit":
                break

            else:
                print("Not a valid response.")

    def run(self):

        while True:
            response = input("What would you like to do? Income, expenses, cash flow, find roi, or quit? ")

            if response.lower() == "income":
                self.income()
            elif response.lower() == "expenses":
                self.expenses()
            elif response.lower() == "cash flow":
                self.cash_flow()
            elif response.lower() == "find roi":
                self.roi()
            elif response.lower() == "quit":
                break
            else:
                print("Not a valid response, try again.")






ari = Calculator()
ari.run()




                

