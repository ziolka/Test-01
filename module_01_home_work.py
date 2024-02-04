# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     repeat = int(input("Enter integer (0 for output): "))      
#     for i in range(repeat):
#         re
#         sum = sum + i
# print(sum)


# repeat = int(input("Ile razy pomnożyć liczbę przez 2? "))
#     for i in range(repeat):
#         num = num * 2
#     print(num)


# stara metoda - działa OK

sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    temp = 0
    temp2 = 0
    if num == 0:
        break
    num = int(input("Enter integer (0 for output): "))
    for i in range (num):
        temp = temp + 1
        temp2 = temp2 + temp
        sum = sum + temp2
print(sum)
