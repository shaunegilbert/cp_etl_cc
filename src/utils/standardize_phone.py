def standardize_phone(phone):
    """Standardizes a phone number to the format (XXX) XXX-XXXX or 1-XXX-XXX-XXXX."""
    
    # Remove all non-digit characters
    phone_digits = ''.join(filter(str.isdigit, str(phone)))
    
    # Format the phone number based on its length and prefix
    if len(phone_digits) == 10:
        return '({}) {}-{}'.format(phone_digits[:3], phone_digits[3:6], phone_digits[6:])
    
    elif len(phone_digits) == 11 and phone_digits.startswith('1'):
        return '1-{}-{}-{}'.format(phone_digits[1:4], phone_digits[4:7], phone_digits[7:])
    
    else:
        return phone