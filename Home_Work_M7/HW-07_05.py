def capital_text(s):
    print(s)
    s = s.capitalize()
    capitalize_chars = (".", "!", "?")
    index = 0
    for char in s:
        if char in capitalize_chars:
            index =  s.find(char) + 1
            if s[index] == " ":
                index_upper = index + 1
                print(s[index_upper])
                letter = s[index_upper].upper()
                s = s[0:index_upper] + s[index_upper].upper() + s[index+2: len(s)]
                print(s)
    return s