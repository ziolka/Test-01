import re


def find_all_emails(text):
    print(f'Text: \n{text}')
    pattern = r'[a-zA-Z]+[^\s]*[a-zA-Z0-9.]+@[a-zA-Z]*[\.]{1}[a-zA-Z]{2,}'
    
    result = re.findall(pattern, text)
    print(f'Result: \n {result}')
    return result