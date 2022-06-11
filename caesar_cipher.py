def caesar_cipher(
    encrypt: str = input('Enter a line of text to encrypt: '), 
    shift: int = input('Enter a shift value as an int between 1 and 25, inclusive: ')
) -> None:
    '''
    takes a string of characters, offsets all alpha code points via shift and prints the new, encoded string with preserved capitalization
    :param encrypt: the string of characters to encode
    :param shift: distance to offset the code points, must be between 1 and 25, inclusive
    '''

    try:
        shift = int(shift)
    except:
        raise Exception('shift must be an int')

    if not (shift >= 1 and shift < 26):
        raise Exception('shift must be between 1 and 25')

    lower_encrypt = [n for n in encrypt.lower()]
    encrypt_value = []
    for i in range(0, len(lower_encrypt)):
        n = lower_encrypt[i]
        if n.isalpha():
            new_val = ord(n) + shift
            if new_val > 122:
                new_val = 97 + (new_val - 122 - 1)
            n = chr(new_val)
            if encrypt[i].isupper():
                n = n.upper()
            encrypt_value.append(n)
        else:
            encrypt_value.append(n)

    encrypt_value = ''.join(encrypt_value)
    print(encrypt_value)
    
if __name__ == '__main__':
    caesar_cipher()
