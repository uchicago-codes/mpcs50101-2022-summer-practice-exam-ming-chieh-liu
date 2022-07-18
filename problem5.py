# Problem 5
# Write a function that identifies if there are common numbers between a pair of lists
# Return True if there is, else return False
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

def common_numbers(a,b):
    """Docstring here"""
    #
    # Your code here
    #
    if is_numbers(a) and is_numbers(b):
        if len(a) > len(b):
            a, b = b, a
        output = False
        for element in a: 
            if element in b:
                output = True 
                break
    else: output = None
    
    return output
  
  

# Test your function with the following lists and assertions
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
c = [10, 11, 12, 13, 14, 15]

assert common_numbers(a,b) == True
assert common_numbers(a,c) == False
assert common_numbers(b,c) == False
