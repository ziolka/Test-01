import re


def find_all_links(text):
    print(f'Text: \n {text}')
    result = []
    iterator = re.finditer(r"https?:\/\/[a-zA-Z]+(\.{1}[a-z]+)+", text)
    for match in iterator:
        result.append(match.group())
    print(f'Result: \n {result}')
    return result