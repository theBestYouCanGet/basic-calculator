def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by 0. "
    return x / y

def main():
    print("Welcome to your Basic Calculator;)")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        operation = input("Chose your Operation(1, 2, 3, 4): ")

        if operation in ['1', '2', '3', '4']:
            x = float(input("Enter x value: "))
            y = float(input("Enter y value: "))

            if operation == '1':
                print("result: ", add(x, y))
            elif operation == '2':
                print("result: ", substract(x, y))
            elif operation == '3':
                print("result: ", multiply(x, y))
            elif operatio == '4':
                print("result: ", divide(x, y))
        else:
            print("Invalid choice")


            next_operation = input("do you want to perform another operation? (yes/no): ")
            if next_operation.lower() != 'yes':
                break

if __name__ == "__main__":
    main()
