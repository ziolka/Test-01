def token_parser(s):
    operators = ['+', '-', '*', '/', '(', ')']
    s1 = []
    if len(s) == 0:
        return s1
    s1 = s.split(" ")
    for item in s1:
        if len(item) >= 2 and not item.isdigit():
            to_split = item
            index = s1.index(item)
            sub_list = []
            for char in to_split:
                sub_list.append(char)
            s1.remove(to_split)
            for item in sub_list:
                s1.insert(index, item)
                index +=1
            print(s1)
    return s1