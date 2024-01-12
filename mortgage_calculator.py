# Class UserInput
class UserInput:

    # Method that takes in a float value and returns it
    def get_float(prompt):
        return float(input(prompt))

    # Method that takes in an integer value and returns it
    def get_int(prompt):
        return int(input(prompt))

# Class MortgageCalculator
class MortgageCalculator:

    # Constructor with instance variables principal, interest_rate and years
    def __init__(self, principal, interest_rate, years):
        self.principal = principal
        self.interest_rate = interest_rate
        self.years = years

    # Method that calculates and returns the monthly_payment
    def calculate_monthly_payment(self):
        monthly_interest_rate = self.interest_rate / 100 / 12
        number_of_payments = self.years * 12
        monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** - number_of_payments)
        return monthly_payment
    
    # Method that uses the get_float and get_int methods from the UserInput class
    def get_user_input(self):
        print("Welcome to the Mortgage Calculator!")
        self.principal = UserInput.get_float("Enter the loan amount (principal): $")
        self.interest_rate = UserInput.get_float("Enter the annual interest rate (%): ")
        self.years = UserInput.get_int("Enter the loan term in years: ")
    
    # Method that launches the calculator in the terminal
    # It displays a summary in the end based on the user's input
    def run_calculator(self):
        self.get_user_input()
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.years * 12
        print("\nMortgage Summary:")
        print(f"Loan Amount: ${self.principal:.2f}")
        print(f"Annual Interest Rate: {self.interest_rate:.2f}%")
        print(f"Loan Term: {self.years} years")
        print(f"Monthly Payment: ${monthly_payment:.2f}")
        print(f"Total Payment: ${total_payment:.2f}")
        
# Instance of the class MortgageCalculator
# The instance variables are set to 0 as they'll be replaced by the user's input
mortgage_calculator = MortgageCalculator(principal=0, interest_rate=0, years=0)
# Launching the calculator
mortgage_calculator.run_calculator()
