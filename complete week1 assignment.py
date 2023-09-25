#print first middle and last character
x="james"
print(x[0:5:2])

#print the middle three characters
y="JhonDipPeta"
print(y[4:7])

# new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
print(s1[0:2]+s2[0:5]+s1[2:4])

#string made of s1 and s2’s first, middle, and last  character
p1 = "America"
p2 = "Japan"
print (p1[0:1]+p2[0:1]+p1[3:4]+p2[2:3]+p1[6:7]+p2[4:5])

#lowercase letters should come first
r1 = "jaMEs"
print (r1[0:2]+r1[4:5]+r1[2:4])


#Count all letters, digits, and special symbols
def count_letters_digits_symbols(word):
    letters = 0
    digits = 0
    symbols = 0

    for char in word:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1
    return letters, digits, symbols

word = input("Enter a word: ")
letter_count, digit_count, symbol_count = count_letters_digits_symbols(word)

print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
print(f"Special Symbols: {symbol_count}")


# mixed String
q1 = "Abc"
q2 = "Xyz"
print(q1[0:1]+q2[2:3]+q1[1:2]+q2[1:2]+q1[2:3]+q2[0:1])


# two strings are balanced or not
def are_strings_balanced(s1, s2):
    t1 = {}
    t2 = {}

    for char in s1:
        t1[char] = t1.get(char, 0) + 1

    for char in s2:
        t2[char] = t2.get(char, 0) + 1

    # Check if all characters in s1 are present in s2
    for char, count in t1.items():
        if char not in t2:
            return False
    return True
# Example usage:
s1 = "japan"
s2 = "iran"
if are_strings_balanced(s1, s2):
    print("true")
else:
    print("false")


#occurrences of “USA” in a given string
def count_usa_occurrences(input_string):
    input_string = input_string.lower()

    count = 0

    start_index = 0

    while True:
        index = input_string.find("usa", start_index)
        if index == -1:
            break

        count += 1
        start_index = index + 3  # Move start_index past the found "usa"
    return count
# Example usage:
input_string = "Welcome to USA. usa awesome, isn't it?"
occurrences = count_usa_occurrences(input_string)
print(f"'USA' occurs {occurrences} times in the given string.")


#sum and average of the digits
def calculate_sum_and_average_of_digits(input_string):
    digit_sum = 0
    digit_count = 0

    for char in input_string:
        if char.isdigit():
            digit_sum += int(char)
            digit_count += 1

    if digit_count > 0:
        digit_average = digit_sum / digit_count
    else:
        digit_average = 0  # Handle the case where there are no digits
    return digit_sum, digit_average
# Example usage:
input_string = "PYnative29@#8496"
sum_of_digits, average_of_digits = calculate_sum_and_average_of_digits(input_string)
print(f"Sum of digits: {sum_of_digits}")
print(f"Average of digits: {average_of_digits}")


#count occurrences of all characters within a string
def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            # If it's not, initialize the count to 1
            char_count[char] = 1
    return char_count

input_string = "Apple"
character_counts = count_characters(input_string)
for char, count in character_counts.items():
    print(f"'{char}' occurs {count} times.")


#count_strings_with_same_first_and_last_char
def count_strings_with_same_first_and_last_char(string_list):
    count = 0
    for s in string_list:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1

    return count

# Example list of strings
input_strings = ['abc', 'xyz', 'aba', '1221']

result = count_strings_with_same_first_and_last_char(input_strings)
print(f"Number of strings with the same first and last character: {result}")


# celsius to fahrenheit
celsius = float(input("Enter a temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")



# Assign your information to variables
name = "Abdul"
last_name = "Rehman"
age = 20
text = f"{name} {last_name} is {age} years old"
print(text)




