number_one = (input)("Enter first number: ")
number_two = (input)("Enter second number: ")

print("The sum is: " + str(int(number_one) + int(number_two)))
print ("The difference is: " + str(int(number_one) - int(number_two)))
print ("The product is: " + str(int(number_one) * int(number_two)))

groceries = ["Milk", "Bread", "Eggs", "Butter", "Apples"]
for idx, item in enumerate(groceries, start=1):
    print(f"{idx}. {item}")

def check_even_odd():
    num = int(input("Enter a number to check if it is even or odd: "))
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Example usage:
check_even_odd()