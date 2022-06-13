def detect_anagram(
    first_word: str = input('Enter your first word: ').lower(),
    second_word: str = input('Enter your second word: ').lower()
):
    '''
    takes two, separate strings and prints if the entered strings are anagrams or not. ignores capitalization and assumes two empty strings are not anagrams
    :param first_word: the first comparison word
    :param second_word: the second comparison word
    '''

    if first_word.isspace() or second_word.isspace():
        print('This is not an anagram')
        return

    first_text = first_word.split()
    first_text = ''.join(first_text)
    second_text = second_word.split()
    second_text = ''.join(second_text)

    first_text = [l for l in first_text]
    second_text = [l for l in second_text]

    while len(first_text) > 0:
        l = first_text[0]
        if l in second_text:
            x = second_text.index(l)
            del first_text[0]
            del second_text[x]
        else:
            del first_text[0]

    if len(first_text) == 0 and len(second_text) == 0:
        print('This is an anagram')
    else:
        print('This is not an anagram')

if __name__ == '__main__':
    detect_anagram()
