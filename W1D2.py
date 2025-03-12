


# daily chalenge Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

# Then, print the first and last characters of the given text.
# The user enters "HelloWorld"
# Then you have to print 
# H
# d


# 3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# HelloWorld


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod





# exercice 1:

# user_input = input("Please enter a string of exactly 10 characters: ")

# input_length = len(user_input)

# if input_length < 10:
#     print("String not long enough")
# elif input_length > 10:
#     print("String too long")
# else:
#     print("Perfect string")







# # exercice 2:

# user_enter = 'hello world'
# print ( user_enter[0])
# print(user_enter[6])






# exercic 3:


# salutation = "Hello"
# for i in range(len(salutation)):
#      print(salutation[:i+1])






# exercice 4:

# import random
# user_input = 'helloworld'

# wed_list = list(user_input)
# random.shuffle(wed_list)
# shuffle_string = ''.join(wed_list)
# print(shuffle_string)