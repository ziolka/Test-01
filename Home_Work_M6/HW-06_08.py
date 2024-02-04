source = [{'name': 'Kovalchuk Oleksiy', 'specialty': 301, 'math': 175, 'lang': 180, 'eng': 155}, {'name': 'Ivanchuk Boryslav', 'specialty': 101, 'math': 135, 'lang': 150, 'eng': 165}, {'name': 'Karpenko Dmitro', 'specialty': 201, 'math': 155, 'lang': 175, 'eng': 185}] 
output = 'output.txt'
def save_applicant_data(source, output):
    
    with open(output, 'w') as f1:
        text = []
        for dict in source:
            print(dict)            
            line = f'{dict["name"]},{dict["specialty"]},{dict["math"]},{dict["lang"]},{dict["eng"]}\n'
            print(f'Line: \n{line}')
            text.append(line)
            print(f'Text: \n{text}')
            
        f1.writelines(text)


save_applicant_data(source, output)