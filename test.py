result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number == True:

        while True:
            operand = input("Podaj liczbę: ")
            try:                    
                part_result = float(operand)
                break
            except ValueError:
                print(f"'{operand}' nie jest liczbą. Spróbuj ponownie")        
    
        if result == None:
            result = part_result
        else:
            result = result

        if operator == "+":
            result = result + part_result
        elif operator == "-":
            result = result - part_result
        elif operator == "*":
            result = result * part_result
        elif operator == "/":
            result = result / part_result
    
        wait_for_number = False

    elif wait_for_number == False:
        
        while True:
            operator = input("Podaj znak matematyczny(+,-,*,/,=): ")
        
            if operator == "+":
                a = 1
            elif operator == "-":
                a = 1
            elif operator == "*":
                a = 1
            elif operator == "/":
                a = 1
            elif operator == "=":
                a = 1
            else:
                a = "b"
            
            try:
                ab = int(a)
                break
            except ValueError:
                print(f" {operator} nie jest '+' lub '-' lub '/' lub '*'. Spróbuj ponownie")
        
        if operator == "=":
            print(result)
            break
        else:
            wait_for_number = True
            continue