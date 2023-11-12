message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
i = 0
for i in range(0,len(message)):
    if message[i] == search:
        result = result + 1
print(result)