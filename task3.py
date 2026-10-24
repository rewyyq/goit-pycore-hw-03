import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
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
normalize_phone(raw_numbers)