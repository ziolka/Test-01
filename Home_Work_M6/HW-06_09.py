def is_equal_string(utf8_string, utf16_string):
    print(f'UTF-8:          {utf8_string}')
    print(f'UTF-16:         {utf16_string}')
    utf8_text = utf8_string.decode('utf-8')
    utf16_text = utf16_string.decode('utf-16')
    print(f'Decoded utf-8: {utf8_text}')
    print(utf8_text == utf16_text)
    if utf8_text == utf16_text:
        return True
    else:
        return False



