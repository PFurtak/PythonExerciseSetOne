# Exercises from week1 schoology
# ask user for name and assign it to a variable
name = input('What is your name? ')

# assign variable to the output
caps = ("Hello, " + name + "!")

# capitalize the output
caps = caps.upper()

# print capitlized output
print(caps)

# find length of name
name_len = len(name)

# assign output string with length and convert integer to string
name_len_output = ("Your name has " + str(name_len) +
                   " letters in it, awesome!")

# capitalize output string
name_len_output_caps = name_len_output.upper()

# print capitalized output
print(name_len_output_caps)
