from art import logo
print(logo)

# Calculator Operations 
def add(n1, n2):            # Addition
    return n1+n2
def sub(n1, n2):            # Subtraction
    return n1-n2
def mul(n1,n2):             # Multiplication
    return n1*n2
def div(n1,n2):             # Division
    return n1/n2

is_complete=False  # state variable of the project

# Created a dictionary of operators
operations={"+":add,
 "-":sub,
 "*":mul,
 "/":div
}

while is_complete==False:
    # Asking the user to enter numbers
    n1=float(input("Enter the first number\n"))
    n2=float(input("Enter the second number\n"))
    
    #  Display the operations to the user
    for key in operations:
        print(key)
        
    # Enter the operation    
    operation_symbol=input("Enter the choice of operation\n")
    
    # calling corresponding function
    if operation_symbol=="+" or operation_symbol=="-" or operation_symbol=="*" or operation_symbol=="/":
        calculation=operations[operation_symbol]
        answer=calculation(n1, n2)
    else:
        print("Invalid Operation\n")
        is_complete=True
        break
    

    
    # Display output
    print(f"{n1} {operation_symbol} {n2} is {answer}")
    
    # Asking the user to continue with calculation or not
    choice=input("Do you want to continue? Yes or No\n").lower()
    if choice=="no":
        is_complete=True
    elif choice=="yes":
        is_complete=False
    else:
        print("invalid entry")
        is_complete=True
    