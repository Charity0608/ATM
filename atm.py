"""A small, interactive ATM console application."""

from getpass import getpass


DEMO_PIN = "1234"
STARTING_BALANCE = 1000.00
MAX_PIN_ATTEMPTS = 3


def read_amount(prompt):
    """Read a positive monetary amount from the user."""
    while True:
        value = input(prompt).strip()
        try:
            amount = float(value)
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        return amount


def main():
    balance = STARTING_BALANCE
    print("=" * 32)
    print("          WELCOME TO ATM")
    print("=" * 32)

    for attempt in range(MAX_PIN_ATTEMPTS):
        pin = getpass("Enter your PIN: ")
        if pin == DEMO_PIN:
            break
        remaining = MAX_PIN_ATTEMPTS - attempt - 1
        if remaining:
            print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
    else:
        print("Too many incorrect attempts. Your session has ended.")
        return

    while True:
        print("\n" + "-" * 32)
        print("              MENU")
        print("-" * 32)
        print("1. Check balance")
        print("2. Deposit cash")
        print("3. Withdraw cash")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            print(f"Your balance is: ${balance:,.2f}")
        elif choice == "2":
            amount = read_amount("Enter deposit amount: $")
            balance += amount
            print(f"${amount:,.2f} deposited successfully.")
            print(f"New balance: ${balance:,.2f}")
        elif choice == "3":
            amount = read_amount("Enter withdrawal amount: $")
            if amount > balance:
                print("Insufficient funds. Your balance has not changed.")
            else:
                balance -= amount
                print(f"Please take your cash: ${amount:,.2f}")
                print(f"Remaining balance: ${balance:,.2f}")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            return
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
