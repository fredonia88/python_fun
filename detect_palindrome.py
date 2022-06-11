def detect_palindrome(
    text: str = input('Enter text: ')
) -> None:
    '''
    takes a string and prints if the entered text is a palindrome or not, assumes two empty strings are not palindromes
    :param text: the string to test 
    '''

    if text.isspace():
        print('This is not a palindrome')
        return

    text = text.split()
    text = ''.join(text)

    new_text = ''
    for w in reversed(text):
        new_text += w

    if text == new_text:
        print('This is a palindrome')
    else:
        print('This is not a palindrome')
        
if __name__ == '__main__':
    detect_palindrome()
