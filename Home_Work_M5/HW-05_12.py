import re


def replace_spam_words(text, spam_words):
    print(f'Text:\n{text}\nWord:\n{spam_words}')
    for word in spam_words:
        pattern = word
        replacement = len(word) * '*'
        result = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        text = result
    print(f'Result: \n{result}')
        
    return result