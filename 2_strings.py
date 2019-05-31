# Strings

# Escape characters - \n, \t, \\

print("=" * 30 + " Raw Strings " + "=" * 30)

# Raw strings
raw = r"this is a \n raw sentence"
print(raw)

print("=" * 30 + " Checks " + "=" * 30)

# Checks
sentence = 'Hello World'
print('Hello' in sentence)
print('Hi' in sentence)

print("=" * 30 + " Lower, Upper " + "=" * 30)

# Lower, Upper
sent = "I love CUPcakes"
print(sent.upper())     # uppercase a string
print(sent.lower())     # lowercase a string
print(sent.isupper())   # check if string is uppercase
print(sent.islower())   # check if string is lowercase

print("=" * 30 + " Other Checks " + "=" * 30)

# Other checks
print(sent.isalpha())
print(sent.isnumeric())
print(sent.isdecimal())
print("12".isnumeric())
print("12".isdecimal())
print("12".isdigit())

print("=" * 30 + " Starts with " + "=" * 30)

# Starts with
sent_2 = "Ruby is walking the dog"
print(sent_2.startswith("Ruby"))
print(sent_2.endswith("dog"))

print("=" * 30 + " Split and Join " + "=" * 30)

# Split and Join
split_up_sent = sent_2.split(' ')
print(split_up_sent)
join_sent = " ".join(split_up_sent)
print(join_sent)

data = 'apple, orange, fruit, cherry'
print(data.split(', '))

print("=" * 30 + " Strip " + "=" * 30)

# Strip
sent_3 = '    This is a sentence      '
print(sent_3.strip() + "|")
print(sent_3.lstrip() + "|")    # strip left side
print(sent_3.rstrip())          # strip right side
