expenses = []


def show_expenses(month):
    print()
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')
    print()


def add_expense(month):
    print()
    expense_amount = int(input("Enter amount [PLN]: "))
    expense_type = input(
        "Enter expense type (food, entertainment, home, other): ")
    print()

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)


def show_stats(month):
    total_amount_this_month = sum(
        expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)

    number_of_amount_this_month = sum(
        1 for _, _, expense_month in expenses if expense_month == month)

    average_amount_this_month = total_amount_this_month / number_of_amount_this_month

    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    average_amount_all = total_amount_all / len(expenses)

    print()
    print("Statistics:")
    print()
    print("All expenses this month [PLN]:", total_amount_this_month)
    print("Average expenses this month [PLN]:", average_amount_this_month)
    print("All expenses [PLN]:", total_amount_all)
    print("Average expenses [PLN]:", average_amount_all)
    print()


while True:
    print()
    month = int(input("Choose month [1-12]: "))
    print()

    if month == 0:
        break

    while True:
        print("0 - Return to month choose.")
        print("1 - Display all expenses.")
        print("2 - Add expense.")
        print("3 - Statistics.")
        print()
        choice = int(input("Choose option: "))

        if choice == 0:
            break

        elif choice == 1:
            show_expenses(month)

        elif choice == 2:
            add_expense(month)

        elif choice == 3:
            show_stats(month)

        else:
            break
