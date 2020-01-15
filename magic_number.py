# prompt user for number, compare to a pre defined number.
# if matching, player wins

MAGICNUMBER = 5

user_input = int(input("What number am I thinking of? "))

if user_input == MAGICNUMBER:
    print("you have won!")
else:
    print("wrong answer.")
