# Write a function that replaces a string within a string and 
# returns the new string

def replace(original, replace, new):
    """Docstring here"""
    #
    # Your code here
    #

    return "something here"



# Test your function
greeting = "Today is Monday!"
revised = replace(greeting, "Monday", "Funday")

# Test for failure
assert revised != "Today is Monday!"

# Test for success
assert revised == "Today is Funday!"
assert replace("Hello World", "Hello", "Goodbye Cruel") == "Goodbye Cruel World"