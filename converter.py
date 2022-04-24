text = input("Enter a string to convert into ascii values:") # insert text to convet
ascii_values = []  # put in list
for character in text:
    ascii_values.append(ord(character)) # transformer
print(ascii_values) # printer
