def repeatedString(s, n):
    core_length = len(s)
    if core_length == 0:
        return 0
    a_counter = 0

    for letter in s:
        if letter.lower() == 'a':
            a_counter += 1

    quotient = n // core_length
    remainder = n % core_length

    return a_counter * quotient + repeatedString(s[:remainder], remainder)


s = "aba"
n = 10

print(repeatedString(s, n))
