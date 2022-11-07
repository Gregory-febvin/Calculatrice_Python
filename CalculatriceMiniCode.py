# Add / Add the two numbers / IN: two numbers / OUT: one number
def add(operator1, operator2):
    result_number = operator1 + operator2
    return result_number

# Substract / Substract the two numbers / IN: two numbers / OUT: one number
def subtract(operator1, operator2):
    return operator1 - operator2

# Multply / Multiply the two numbers / IN: two numbers / OUT: one number
def multiply(operator1, operator2):
    return operator1 * operator2

# Divide / Divide the two numbers / IN: two numbers / OUT: one number
def divide(operator1, operator2):
    if operator2 == 0:
        return None
    return operator1 / operator2

# Posting_Result / Print the result in the console / IN: one number / OUT: nothing
def Posting(finalResult):
    if finalResult == None :
        print("Division Imposible")
        return

    print("Le resultat est : {}".format(finalResult))

# Choose_Operation / Make the user chose two numbers for the operation / IN: two numbers / OUT: nothing
def OperationChoice(operation_number):
    operator1 = float(input("Entre ton premier nombre: "))
    operator2 = float(input("Entre un second nombre: "))
    

    if operation_number == '1':
        result = add(operator1, operator2)
        Posting(result)        

    elif operation_number == '2':
        result = subtract(operator1, operator2)
        Posting(result)  

    elif operation_number == '3':
        result = multiply(operator1, operator2)
        Posting(result)  

    elif operation_number == '4':
        result = divide(operator1, operator2)
        Posting(result)  
        

# Main_Program / Let the user choose the operation and let him do another one / IN: one number OR oui|non / OUT: nothing
while True:

    print("Selectione une opération :")
    print("1 . Addition")
    print("2 . Soustraction")
    print("3 . Multiplication")
    print("4 . Division")

    operation_number = input("Entre ton choix(1/2/3/4): ")

    if operation_number in ('1', '2', '3', '4'):
        OperationChoice(operation_number)

        next_calculation = input("Un autre calcul? (oui/non): ")
        if next_calculation == "non":
          break
    else:
        print("Entré Invalide")