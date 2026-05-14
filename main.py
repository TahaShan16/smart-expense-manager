from manager import ExpenseManager

manager = ExpenseManager()

while True:
    print("""
=============================
   Smart Expense Manager
=============================
1. Create Account
2. Login
3. Add Expense
4. View Expenses
5. Delete Expense
6. View Insights
7. Exit
=============================
""")
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        manager.create_account()
    elif choice == "2":
        manager.login()
    elif choice == "3":
        manager.add_expense()
    elif choice == "4":
        manager.view_expenses()
    elif choice == "5":
        manager.delete_expense()
    elif choice == "6":
        manager.view_insights()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
