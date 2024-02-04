try:
    result = 10 / 0
except ZeroDivisionError:
    print("Nie dzielimy przez 0.")
finally:
    print("To jest zawsze wykonywane")