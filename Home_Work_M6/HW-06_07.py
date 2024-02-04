def sanitize_file(source, output):
    print(f'Source: \n {source}\nOutput: \n {output}')
    with open(source, 'r') as f1:
        while True:
            raw_text = f1.readline()
            print(f'Raw text: \n {raw_text}')
            if not raw_text:
                break
            for i in raw_text:
                if i.isdigit():
                    raw_text = raw_text.replace(i, "")
            sanitized_text = raw_text
            print(f'Sanitized text: \n {sanitized_text}')

    with open(output, 'w') as f2:
            f2.write(sanitized_text)     
    
    return output
