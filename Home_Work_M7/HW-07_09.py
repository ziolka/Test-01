def all_sub_lists(data):
    print(data)
    all_lists = []
    empty_list = []
    sub_list_4 = []
    print(len(data))
    index = 1
    all_lists.insert(0, empty_list)
    if data == []:
        return all_lists
    for list in data:
        sub_list_1 = [list]
        all_lists.insert(index, sub_list_1)
        index +=1
    m = 0
    for list in data:
        if m < len(data)-1:
            x1 = data[m]
            x2 = (data[m+1])
            sub_list_2 = [x1, x2]
            all_lists.append(sub_list_2)
            m +=1
            print(m)
    n = 0
    for list in data:
        if n < len(data)-2:
            y1 = data[n]
            y2 = (data[n+1])
            y3 = (data[n+2])
            sub_list_3 = [y1, y2, y3]
            all_lists.append(sub_list_3)
            n +=1
            print(n)
    for list in data:
        print(f'--- {list}')
        sub_list_4.append(list)
    all_lists.append(sub_list_4)
    print(all_lists)
    return all_lists
    
    
    
        
            
    