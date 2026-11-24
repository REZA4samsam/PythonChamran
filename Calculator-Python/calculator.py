
import os

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def calculator():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(CYAN + "=" * 40)
        print("       PYTHON CALCULATOR")
        print("=" * 40 + RESET)

        print(GREEN + """
        Info:
        [E] Exit
        [A] Again
        """ + RESET)

        print(BLUE + "-" * 40 + RESET)

        choice = input(YELLOW + "(+)(-)(*)(/)(×)(÷) Choose one of them: " + RESET)

        if choice.lower() == "e":
            print(RED + "\n Good bye!" + RESET)
            break

        if choice not in ["+", "-", "*", "/", "×", "÷"]:
            print(RED + "\n Your choice is incorrect!!" + RESET)
            input("\n Enter to continue...")
            continue

        try:
            num1 = float(input("\n NUMBER: "))
            num2 = float(input(" NUMBER: "))

            if choice == "+":
                result = num1 + num2
                symbol = "+"

            elif choice == "-":
                result = num1 - num2
                symbol = "-"

            elif choice in ["*", "×"]:
                result = num1 * num2
                symbol = "×"

            elif choice in ["/", "÷"]:
                if num2 == 0:
                    print(RED + "\n Cannot divide by zero!" + RESET)
                    input("\n Press ENTER to continue...")
                    continue

                result = num1 / num2
                symbol = "÷"

            print(GREEN + "\n" + "=" * 40)
            print(f" RESULT: {num1:g} {symbol} {num2:g} = {result:g}")
            print("=" * 40 + RESET)

        except ValueError:
            print(RED + "\n Please enter a valid number!" + RESET)

        # Calculate again or exit
        again = input("\n A for CALCULATE or E for EXIT: ")

        if again.lower() == "e":
            print(RED + "\n Goodbye!" + RESET)
            break

        elif again.lower() == "a":
            continue

        else:
            print(RED + "\n Invalid choice!" + RESET)
            input("\n Press ENTER to continue...")
            continue


calculator()
