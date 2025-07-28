""" The change include user data validation"""
dividende = 0
divisor = 0

while True:
    # check if the dividend is valid
    try:            
        dividende = int(input("Enter the dividende: "))
        if dividende < 0:
            print("\n\t the dividend should be positive" + "!" * 5)
            continue
        else:
            break
    except:
        print("\n\tEnter a valid number")

while True:
    # Check if the divisor is valid
    try:            
        divisor = int(input("Enter the divisor: "))
        if divisor < 0:
            print("\n\t the divisor  should be positive" + "!" * 5)
            continue

        elif divisor == 0:
            print("\n\t We can't divide a number by 0 ")
        else:
            break
    except:
        print("\n\tEnter a valid number")

dividende = int(input("Enter the dividende: "))
divisor = int(input("Enter the divisor: "))

quotient = dividende//divisor
rest = dividende % divisor

print(f"the division of {dividende} and {divisor} give :\n quotient: {quotient}\n rest: {rest}")