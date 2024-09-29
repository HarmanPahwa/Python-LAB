user_input = input("Enter a string: ")

vowels = "aeiouAEIOU"

# Count the number of vowels in the string
vowel_count = sum(1 for char in user_input if char in vowels)

print("Number of vowels in the string:", vowel_count)