# Write a function to calculate the sum ofthe odd numbers in a list of numbers. 
# The function should return the sum. Ensure that that list 
# contains only numbers. If not return the value `None`.


def sum_of_odds(numbers):
    s = 0
    for number in numbers:
        if number % 2 == 1: 
            s += number
    return s


assert sum_of_odds([1,1,2,9,1]) == 5
assert sum_of_odds([1,2,10,10,3]) != 10
assert sum_of_odds([1,2,3,4,"a","b","c"]) == None