import re


def find_all_words(text, word):
    print(f'Text:\n{text}\nWord:\n{word}')

    list = []

    check = re.findall(word, text, flags=re.IGNORECASE)
    print(f'Check result: {check}')

    list = check
    print(f'List: \n {list}')

    return list