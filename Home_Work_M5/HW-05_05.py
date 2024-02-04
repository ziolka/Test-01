def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    # print(f'Raw phone number: {phone}')
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    print(list_phones)
    jp = [] #81
    sg = [] #65
    tw = [] #886
    ua = [] #380
    phone_prefix = None
    for phones in list_phones:
        phone = sanitize_phone_number(phones)
        print(f'Phone is: {phone}')
               
        if phone.startswith("81") == True:
            jp.append(phone)
        elif phone.startswith("65") == True:
            sg.append(phone)
        elif phone.startswith("886") == True:
            tw.append(phone)
        else:
            ua.append(phone)
        print(f'JP: {jp}')
        print(f'SG: {sg}')
        print(f'TW: {tw}')        
        print(f'UA: {ua}')
    
    sorted_phones = {
        "UA": ua,
        "JP": jp,
        "TW": tw,
        "SG": sg
    }
    print(f'Sorted phones: {sorted_phones}')

    return sorted_phones

