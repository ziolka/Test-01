import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
cat_dict = {}
cat_dict_list = []
cat_tuple = {}
cat_tuple_list = []
def convert_list(cats):
    print(f'Cats: {cats}')
    print(type(cats))
    if len(cats) == 0:
        return None
    
    if isinstance(cats[0], Cat):
        print("+++")
        for cat in cats:
            cat_dict = {
            "nickname": cat.nickname,
            "age": cat.age,
            "owner": cat.owner
            }
            print(cat_dict)
            cat_dict_list.append(cat_dict)
        
        print(f'Finally: {cat_dict_list}')
        return cat_dict_list  
    else:
        for entry in cats:
            print(entry)
            cat_tuple = Cat(entry["nickname"], entry["age"], entry["owner"])
            
            print(f'Cat tuple: {cat_tuple}')
            cat_tuple_list.append(cat_tuple)
            print(f'Finally cat tuple list: {cat_tuple_list}')

        return cat_tuple_list     