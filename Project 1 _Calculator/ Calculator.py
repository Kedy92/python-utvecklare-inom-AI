def calculation():
    # Funktion som utför en enkel miniräknare
    
    while True:  # Upprepa tills användaren matar in giltiga värden
        try:
            # Tar emot första talet från användaren och omvandlar det till flyttal
            num1 = float(input("Enter num1>>>"))
            
            # Frågar efter operatorn (+, -, *, /)
            operation = input("Enter operator (+, -, *, /): >>>")
            
            # Tar emot andra talet
            num2 = float(input("Enter num2>>>"))
            
            # Utför beräkning beroende på vald operator
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            elif not operation:
                print("Error: Invalid operator! Please use +, -, * or /")
            else:
                # Om användaren skrev något annat än + - * /
                print("Error: Invalid operator! Please use +, -, * or /")
                continue  # Börja om loopen
            
            # Skriver ut resultatet i ett tydligt format
            print(f"The result of {num1} {operation} {num2} is: {result}")
            break  # Avsluta loopen om allt gick bra
        
        # Fångar fel när användaren inte skriver in siffror
        except ValueError:
            print("Error: Please enter numeric values.")
    
        # Fångar fel om användaren försöker dividera med 0
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

# Kör programmet
calculation()