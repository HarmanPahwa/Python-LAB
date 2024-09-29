# A. Separate the string into comma-separated values
X = "India.is.my.country"
comma_separated = X.replace('.', ',')
print("Comma-separated values:", comma_separated)

# B. Remove a given character from a string
Y = "M.A.N.I.P.A.L"
char_to_remove = 'A'  # Example character to remove
removed_character = Y.replace(char_to_remove, '')
print("String after removing character '{}': {}".format(char_to_remove, removed_character))

# C. Remove the (.) dots from the above string
dots_removed = Y.replace('.', '')
print("String after removing dots:", dots_removed)
