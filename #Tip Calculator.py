# Tip Calculator
def tip_calculator():
    print("Welcome to the Tip Calculator!")
    print("I'll help you calculate the tip and split the bill.")

    try:
        total_bill = float(input("Enter the total bill amount: $"))
        tip_percentage = float(input("Enter the tip percentage you'd like to give (e.g., 15 for 15%): "))
        num_people = int(input("Enter the number of people to split the bill: "))
        
        if total_bill < 0 or tip_percentage < 0 or num_people <= 0:
            print("Invalid input. Please enter positive values.")
            return

        # Calculate the tip amount, total bill, and amount per person
        tip_amount = (tip_percentage / 100) * total_bill
        total_amount = total_bill + tip_amount
        amount_per_person = total_amount / num_people

        print(f"\nTip Amount: ${tip_amount:.2f}")
        print(f"Total Bill with Tip: ${total_amount:.2f}")
        print(f"Amount Per Person: ${amount_per_person:.2f}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Run the Tip Calculator
tip_calculator()
