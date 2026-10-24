import re
normalized_numbers = []
def normalize_phone(phone_numbers: list) -> str:
    pattern = r"\d*"        #pattern for digits
    for num in phone_numbers:
        normalized_num = re.findall(pattern, num)   #findall digits with pattern
        normalized_num = "".join(normalized_num)    #.join to make str 
        if normalized_num.startswith("0"):
            normalized_num = "+38" + normalized_num
            normalized_numbers.append(normalized_num)        #check if phone number starts with 0 or 380, adding +38 or just +
        elif normalized_num.startswith("380"):
            normalized_num = "+" + normalized_num
            normalized_numbers.append(normalized_num)
    return print(f"Нормалізовані номери телефонів для SMS-розсилки: {normalized_numbers}")