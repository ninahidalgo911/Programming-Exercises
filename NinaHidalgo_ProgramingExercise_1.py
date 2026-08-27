# This program is asking the user for how many tickets they would like to purchase

def how_many_tickets():
    # This is the first function.

    #Brief Description:
    #Gets the number of tickets the buyer would like to purchase and
    #confirms if that the amount is within the allowed limit.

    #Parameters:
    #None

    #Variables:
    #tickets - int

    #Logical Steps:
    #1. Ask the buyer how many tickets they would like to purchase.
    #2. Check if the amount is greater than 4.
    #3. If the amount is greater than 4, ask the buyer for the amount again.
    #4. Return the number of tickets.

    #Return:
    #Returns the number of tickets the buyer would like to purchase.


    tickets = int(input("How many tickets would you like? "))

    # Validation logic.
    while tickets > 4:
        print("That amount is over the limit.")

        # Ask for the number again.
        tickets = int(input("How many tickets would you like? "))

    return tickets


def sold_tickets():
    # This is the second function.
    tickets_remaining = 20
    buyers = 0

    while tickets_remaining > 0:
        tickets_requested = how_many_tickets()

        tickets_remaining = tickets_remaining - tickets_requested

        buyers = buyers + 1

        print("Remaining tickets:", tickets_remaining)

    print("Total number of buyers:", buyers)


if __name__ == "__main__":
    sold_tickets()
