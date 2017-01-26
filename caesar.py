def alphabet_position(letter):
    letter = letter.lower()

    value = ord(letter) - ord('a')

    return value

def rotate_character(char, rot):
    if char.isalpha():

        upper = False
        if char.isupper():
            upper = True

        pos = alphabet_position(char)
        pos = (pos + rot) % 26

        pos = pos + ord('a')
        char = chr(pos)

        if upper:
            char = char.upper()

    return char

def encrypt(text, to_rotate):
    encrypted = ''

    for char in text:
        encrypted += rotate_character(char, to_rotate)

    return encrypted
