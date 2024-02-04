def is_integer(s):
    print(s)
    if len(s) == 0:
        return False
    else:
        s = s.strip()
        if len(s) == 0:
            return False
        
        else:
            print(s)
            print(s[0])
            if s[0] == "+" or s[0] == "-":
                s = s[1:]
                print(s)
                if s.isdigit():
                    result = True
                    print(result)
            else:
                result = False
                print(result)
        
    return result