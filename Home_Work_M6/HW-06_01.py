def total_salary(path):
    f = open(path, 'r')
    total_salary = 0
    while True:
        salary = []
        # total_salary = 0
        line = f.readline()
        if not line:
            break
        print(line)
        for char in line:
            if char.isdigit():
                salary.append(char)
                amount = "".join(salary)
        total_salary += float(amount)
                
        print(f'Salary: {salary}')
        print(f'Amount: {amount}')
        print(f'Total Salary: {total_salary}')

    f.close()
    return total_salary
    
