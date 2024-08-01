try:
    num2 = float(input("Enter the input "))
    num1 = float(input("Enter the input "))
    print("Result = {}".format(num1 + num2))
except ValueError:
    print("Incorrect input is provided, Check the input and try again.")