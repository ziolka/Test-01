result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        try:
            operand_input = float(input("Podaj liczbę: "))
            if result is None:
                result = operand_input
            else:
                if operator == "+":
                    result += operand_input
                elif operator == "-":
                    result -= operand_input
                elif operator == "*":
                    result *= operand_input
                elif operator == "/":
                    if operand_input != 0:
                        result /= operand_input
                    else:
                        print("Nie można dzielić przez zero")
                        continue
            operand = None
            operator = None
            wait_for_number = False
        except ValueError:
            print("Nieprawidłowa liczba")
    else:
        operator_input = input("Podaj operator (+, -, *, /, =): ")
        if operator_input not in ["+", "-", "*", "/", "="]:
            print("Nieznany operator")
        elif operator_input == "=":
            if result is not None:
                print(f"The final result is: {result}")
            else:
                print("Brak danych do wyświetlenia wyniku")
            break
        else:
            if operator is not None:
                print("Operator wprowadzony dwa razy z rzędu")
            else:
                operator = operator_input
                wait_for_number = True