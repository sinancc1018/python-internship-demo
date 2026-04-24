
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")


choice = int(input("Enter choice : "))

if choice == 1:
    print("Result:", num1 + num2)

elif choice == 2:
    print("Result:", num1 - num2)

elif choice == 3:
    print("Result:", num1 * num2)

elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by zero is not allowed")

else:
    print("Invalid choice")
