# Write a function to calculate the sum ofthe odd numbers in a list of numbers. 
# The function should return the sum. Ensure that that list 
# contains only numbers. If not return the value `None`.

def is_numbers(numbers):
    """check whether the input is a list of numbers
    input(list or tuple): a list of numbers
    output(bool): if the type of the input is correct, return True; otherwise, return False
    """
    TF_numbers = False
    # if the type of the input is a list and elements in the list are all numbers
    if type(numbers) == list or type(numbers) == tuple:
        TF_numbers = True
        for number in numbers:
            if type(number) != int and type(number) != float:
                TF_numbers = False
                break
    
    return TF_numbers

def sum_of_odds(numbers):
    s = 0
    if is_numbers(numbers):
        for number in numbers:
            if number % 2 == 1: 
                s += number
    else:
        s = None
    return s


assert sum_of_odds([1,1,2,9,1]) == 12
assert sum_of_odds([1,2,10,10,3]) != 10
assert sum_of_odds([1,2,3,4,"a","b","c"]) == None