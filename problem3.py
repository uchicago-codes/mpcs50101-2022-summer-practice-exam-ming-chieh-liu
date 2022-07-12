# Write a function that replaces a string within a string and 
# returns the new string

def replace(original, replace_word, new):
    """Docstring here"""
    #
    # Your code here
    #
    length_of_word = len(replace_word)
    try:
        index = original.index(replace_word)
    except:
        return original
    else:
        new_word = original[:index] + new + original[index+length_of_word:]
        output = replace(new_word, replace_word, new)
        return output

# Test your function
greeting = "Today is Monday!"
revised = replace(greeting, "Monday", "Funday")
print(revised)

# Test for failure
assert revised != "Today is Monday!"

# Test for success
assert revised == "Today is Funday!"
assert replace("Hello World", "Hello", "Goodbye Cruel") == "Goodbye Cruel World"