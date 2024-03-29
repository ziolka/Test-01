def normalize_name(file_name):
    ''' 
    Replaces special characters in file and folder names. 
    '''
    new_name = (
    file_name.replace("ą", "a")
    .replace("Ą", "A")
    .replace("ć", "c")
    .replace("Ć", "C")
    .replace("ę", "e")
    .replace("Ę", "E")
    .replace("ń", "n")
    .replace("Ń", "N")
    .replace("ó", "o")
    .replace("Ó", "O")
    .replace("ś", "s")
    .replace("Ś", "S")
    .replace("ź", "z")
    .replace("Ź", "Z")
    .replace("ż", "z")
    .replace("Ż", "Z")
    .replace("!", "_")
    .replace("@", "_")
    .replace("#", "_")
    .replace("$", "_")
    .replace("%", "_")
    .replace("^", "_")
    .replace("&", "_")
    .replace("*", "_")
    .replace("(", "_")
    .replace(")", "_")
    .replace("[", "_")
    .replace("]", "_")
    .replace("{", "_")
    .replace("}", "_")
    .replace("-", "_")
    .replace("+", "_")
    .replace("+", "_")
    .replace(",", "_")
    .replace("'", "_")
    .replace('"', "_")
    .replace("/", "_")
    .replace("=", "_")
    .replace(" ", "_")
    )
    return new_name

if __name__ == '__main__':
    normalize_name('ąĆÓś-ą@#12/3[}4$%^&"AĄ')
