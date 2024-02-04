def format_phone_number(func):
    def inner(phone):
        print(f'Phone number: {phone}')
        sanitized_phone = func(phone)
        print(f'Formatted phone number: {sanitized_phone}')
        if len(sanitized_phone) == 12:
            formatted_phone = "+" + sanitized_phone
        else:
            formatted_phone = "+38" + sanitized_phone
        return formatted_phone
        print(f'Formatted phone number: {formatted_phone}')
    return inner

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone