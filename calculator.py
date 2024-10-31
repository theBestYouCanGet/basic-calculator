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
    print("Welcome to your Basic Calculator")
    
    while True:
        print("Select your operation: ")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        operation = input("Chose your Operation(1, 2, 3, 4): ")

        if operation in ['1', '2', '3', '4']:
            try:
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
        
            except ValueErroe:
                print("Invalid input! Please enter numbers only.")
        
        elif operation == '5':
            print("Exiting the calculator. Goodbye! ")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
