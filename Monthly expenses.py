# Monthly Expenses
# program finds the total, highest, and lowest expenses.

from functools import reduce


# Get the total of all expenses
def get_total(expenses):
    return reduce(lambda total, expense: total + expense[1], expenses, 0)


# Get the highest expense
def get_highest(expenses):
    return reduce(lambda x, y: x if x[1] > y[1] else y, expenses)


# Get the lowest expense
def get_lowest(expenses):
    return reduce(lambda x, y: x if x[1] < y[1] else y, expenses)


# Main program
def main():

    expenses = []

    # Ask how many expenses the user has
    number = int(input("How many expenses do you have? "))

    # Get each expense
    for i in range(number):
        name = input("Enter the expense type: ")
        amount = float(input("Enter the expense amount: "))

        # Add the expense to the list
        expenses.append((name, amount))

    # Calculate the expenses
    total = get_total(expenses)
    highest = get_highest(expenses)
    lowest = get_lowest(expenses)

    # Display the results
    print("\nMonthly Expenses")
    print("Total expense: $" + format(total, ".2f"))
    print("Highest expense: " + highest[0] + " - $" + format(highest[1], ".2f"))
    print("Lowest expense: " + lowest[0] + " - $" + format(lowest[1], ".2f"))


# Start the program
main()