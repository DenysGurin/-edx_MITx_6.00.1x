def FancyDivide(list_of_numbers, index):
    try:
        demon = list_of_numbers[index]
        return [SimpleDivide(item, demon) for item in list_of_numbers]
        
    except ZeroDivisionError:
        return [0 for item in list_of_numbers]
    
def SimpleDivide(item, demon):
    return item / demon
    
    
print FancyDivide([0, 2, 4], 0)