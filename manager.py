from expense import Expense
from file_handler import load_users, save_users
from user import User
import exceptions

class ExpenseManager:
    def __init__(self):
        self.users = load_users()
        self.current_user = None

    def create_account(self):
        name = input("Enter your name: ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        if username in self.users:
            raise exceptions.WrongUserNameError("Username already exists.")
        else:
            new_user = User(name, username, password)
            self.users[username] = new_user
            save_users({username: user.to_dict() for username, user in self.users.items()})
            print("Account created successfully.")

    def login (self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.users:
            user = self.users[username]
            if user.password == password:
                self.current_user = user
                print("Login successful.")
            else:
                raise exceptions.WrongPasswordError("Incorrect password.")
        else:
            raise exceptions.WrongUserNameError("Username does not exist.")

    def add_expense(self):
        if self.current_user is None:
            print("Please log in to add an expense.")
            return
        
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: ")
        date = input("Enter the expense date (YYYY-MM-DD): ")
        description = input("Enter a description for the expense: ")
        expense = Expense(amount, category, date, description)
        self.current_user.expenses.append(expense)
        save_users({username: user.to_dict() for username, user in self.users.items()})

    def view_expenses(self):
        if self.current_user is None:
            print("Please log in to view expenses.")
            return
        
        if not self.current_user.expenses:
            print("No expenses recorded.")
            return
        
        for expense in self.current_user.expenses:
            print(f"Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}, Description: {expense.description}")  
        

    def delete_expense(self):
        if self.current_user is None:
            print("Please log in to delete an expense.")
            return
        
        if not self.current_user.expenses:
            print("No expenses recorded.")
            return
        for index, expense in enumerate(self.current_user.expenses):
            print(f"{index + 1}. Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}, Description: {expense.description}")

        choice = int(input("Enter the number of the expense to delete: "))
        if 1 <= choice <= len(self.current_user.expenses):        
            del self.current_user.expenses[choice - 1]
            save_users({username: user.to_dict() for username, user in self.users.items()})
            print("Expense deleted successfully.")
        else:
            print("Invalid choice.")
        

    def view_insights(self):
        if self.current_user is None:
            print("Please log in to view insights.")
            return
        
        if not self.current_user.expenses:
            print("No expenses recorded.")
            return
        
        total = sum(expense.amount for expense in self.current_user.expenses)
        print(f"Total Spending: {total}")
        
        category_totals = {}
        for expense in self.current_user.expenses:
            category_totals[expense.category] = category_totals.get(expense.category, 0) + expense.amount
        
        most_used = max(category_totals, key=category_totals.get)
        print(f"Most spent category: {most_used}")

        for category, amount in category_totals.items():
            percentage = (amount / total) * 100
            if percentage > 40:
                print(f"Warning: You spent {percentage:.1f}% on {category} - consider reducing!")

        print("Expense Insights:")
        for category, total in category_totals.items():
            print(f"Category: {category}, Total Spent: {total}")