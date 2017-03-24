import string

def alphabet_position(letter):
    if letter in string.ascii_letters:
        return string.ascii_letters.find(letter)%26




def rotate_character(char, rot):
    if char in string.ascii_letters:
        start_idx = alphabet_position(char)
        new_idx = (start_idx + rot)%26
        if char in string.ascii_lowercase:
            return string.ascii_lowercase[new_idx]
        elif char in string.ascii_uppercase:
            return string.ascii_uppercase[new_idx]
    else:
        return char



def encrypt(text, rot):
    etext = ""
    for i in text:
        etext += str(rotate_character(i, rot))
    return etext
