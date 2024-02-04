pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity # dzielenie bez
except ZeroDivisionError:
    print('Divide by zero completed!')