def solve_riddle(riddle, word_length, start_letter, reverse=False):
    result = ""
    index = 0
    if reverse == False:
        for char in riddle:
            if char == start_letter:
                index = riddle.find(char)
                result = riddle[index:index+word_length]
    else:
        for char in reversed(range(-len(riddle), 0)):
            if riddle[char] == start_letter:
                result = riddle[char-word_length+1:char+1]
                result = str(result)[::-1]

    return result