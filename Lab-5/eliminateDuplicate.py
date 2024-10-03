sequence = "aAbBcCdD"
unique_chars = list(set(sequence))
upper_lower = list(map(lambda x: (x.upper(), x.lower()), unique_chars))
print(upper_lower)
