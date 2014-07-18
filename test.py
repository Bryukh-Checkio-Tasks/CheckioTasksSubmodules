def checkio(data): 
    numerals = {'M' : 1000, 'D': 500, 'C' : 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1} 
    end_result = "" 
    new_result = "" 
    for key in numerals: 
        while True:  
            new_result, data, flag = check(data, key, numerals[key]) 
            if not flag: 
                break 
            else: 
                end_result += new_result  
    return end_result 
 
def check(data, key, value): 
    result = "" 
    flag = True 
    if data - value >= 0: 
        result += key 
        data -= value     
    else: 
        flag = False 
    return result, data, flag

print(checkio(10))