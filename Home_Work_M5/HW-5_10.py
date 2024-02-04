import re


def find_word(text, word):
    print(f'Text:\n{text}\nWord:\n{word}')
    dict = {
        'result': False,
        'first_index': None,
        'last_index': None,
        'search_string': word.lower(),
        'string': text
    }
    
    check = re.search(word, text)
    print(f'Check result: {check}')

    if check:
        dict['result'] = True
        dict['first_index'] = check.span()[0]
        dict['last_index'] = check.span()[1]
        dict['search_string'] = word
        dict['string'] = text

    return dict
        
    