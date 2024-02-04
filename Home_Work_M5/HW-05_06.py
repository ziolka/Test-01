def is_spam_words(text, spam_words, space_around=False):
    print(f'Text is: {text}')
    print(f'Spam words: {spam_words}')
    print(f'Space around parameter is: {space_around}')
    unitext = text.lower()
    print(f'Text.lower is: {unitext}')
    result = None

    if space_around == False:
        for word in spam_words:

            word = word.replace("'", "")
            print(f'Word without: {word}')
            
            check = unitext.find(word)
            print(check)
            if check >= 0:
                result = True
            else:
                result = False
            print(f'Result: {result}')
    else:
        for word in spam_words:
            pattern = " " + word + " "
            check = unitext.find(pattern)
            print(check)
            if check >= 0:
                result = True
            else:
                result = False
            print(f'Result: {result}')

    return result
    
    
# print(is_spam_words('The aftermath reaches far.', 'match', space_around=False))

  
        
    
    
        
        
            
                
                    
                        
                
                    
                        
                    
                        
            
                
    