def find_a_word(
    test: str = input('Enter a word to search for: ').lower(),
    my_string: str = input('Enter a string to search through: ').lower()
):
    '''
    takes a word to search for and word to search through. prints a statement if all letters of the test word are sequentially found in my_string, or not.
    :param test: the word to search for
    :param my_string: the word to search through
    '''

start = 0
x = 0
for l in test:
    x = my_string[x:].find(l)
    if x == - 1:
        print('This word is not found')
        break
    else:
        start += 1
        if start > len(test):
            print('This word is found')
        
if __name__ == '__main__':
    find_a_word()
