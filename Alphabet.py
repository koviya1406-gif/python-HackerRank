import string
def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = (size * 4) - 3
    lines = []
    for i in range(size):
        s = alphabet[size - i - 1 : size]        
        row_letters = list(s[::-1] + s[1:])
        line = "-".join(row_letters)
        lines.append(line.center(width, "-"))
    result = lines + lines[::-1][1:]
    print("\n".join(result))
