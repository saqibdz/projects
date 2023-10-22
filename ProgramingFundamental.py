class PersonalFinanceTracker:
  def __init__(self):
      self.income = 0
      self.expenses = []

  def add_income(self, amount):
      self.income += amount

  def add_expense(self, category, amount):
      self.expenses.append({"category": category, "amount": amount})

  def calculate_balance(self):
      total_expenses = sum(item["amount"] for item in self.expenses)
      balance = self.income - total_expenses
      return balance

  def display_summary(self):
      print("Personal Finance Summary")
      print("----------------------------")
      print(f"Income: ${self.income}")
      print("Expenses:")
      for expense in self.expenses:
          print(f"{expense['category']}: ${expense['amount']}")
      print("----------------------------")
      balance = self.calculate_balance()
      print(f"Balance: ${balance}")

def main():
  finance_tracker = PersonalFinanceTracker()

  while True:
      print("\nOptions:")
      print("1. Add Income")
      print("2. Add Expense")
      print("3. Display Summary")
      print("4. Quit")

      choice = input("Select an option: ")

      if choice == "1":
          income = float(input("Enter income amount: $"))
          finance_tracker.add_income(income)
      elif choice == "2":
          category = input("Enter expense category: ")
          amount = float(input("Enter expense amount: $"))
          finance_tracker.add_expense(category, amount)
      elif choice == "3":
          finance_tracker.display_summary()
      elif choice == "4":
          print("Exiting the program.")
          break
      else:
          print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
  main()
