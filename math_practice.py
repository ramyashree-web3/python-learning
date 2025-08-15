# Safe integer input
def get_int(prompt):
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("Invalid integer! Please try again.")

            while True:
                print("---- New Calculation ----")
            num1 = get_int("Enter a number: ")
            num2 = get_int("Enter another number ")

            print("Choose an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")

            choice = get_int("Enter the number of your choice: ")

            if choice == 1:
                result = num1 = num2
                print("The sum is:", result)
            elif choice == 2:
                result = num1 - num2
                print("The diiference is:", result)
            elif choice == 3:
                result = num1 * num2
                print("The product is:", result)
            elif choice == 4:
                if num2 != 0:
                    result = num1 / num2
                    print("The quotient is:", result)
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid choice1 Please select between 1 and 4.")



                             
