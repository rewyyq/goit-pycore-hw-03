import random
def get_numbers_ticket(min: int, max: int, quantity: int) ->list[int]:
    min_value = 1
    max_value = 1000
    try:
        if min < min_value:
            return []
        elif max > max_value:
            return []
        elif quantity < min or quantity > max:
            return []
        else: 
            res = random.sample(range(min, max+1), quantity)  #create list with unique numbers in range from min max and quantity
            res.sort()
            return res
    except TypeError:
        print("Wrong type!")