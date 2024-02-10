def custom_iterator(max_value):
    current_value = 0
    while current_value < max_value:
        yield current_value
        current_value += 1

c = custom_iterator(10)
for i in c:
    print(i)