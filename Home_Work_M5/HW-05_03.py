import re

def sanitize_phone_number(phone):
    del_chars = re.sub(r'(\+|\-|\(|\)|\s)', '', phone)
    # stripped_text = del_chars.strip()

    return del_chars
    
        
print(sanitize_phone_number('  +23 461 230 989   -'))