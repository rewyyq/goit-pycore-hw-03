import re
def normalize_phone(phone_number: str) -> str:
    pattern = r"\d*"        #pattern for digits
    normalized_num = re.findall(pattern, phone_number)   #findall digits with pattern
    normalized_num = "".join(normalized_num)    #.join to make str 
    if normalized_num.startswith("0"):
        normalized_num = "+38" + normalized_num
    elif normalized_num.startswith("380"):#check if phone number starts with 0 or 380, adding +38 or just +
        normalized_num = "+" + normalized_num
    return normalized_num