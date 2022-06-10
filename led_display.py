def led_display(digits: int = input('Enter any number of integers ')) -> None:
    '''
    prints each digit in digits in an led display type format
    :param digits: the numbers to be displayed
    '''

    l = ['#  ', '  #', '# #', '###']

    digit_map = {
        '1': [l[1], l[1], l[1], l[1], l[1]],
        '2': [l[3], l[1], l[3], l[0], l[3]],
        '3': [l[3], l[1], l[3], l[1], l[3]],
        '4': [l[2], l[2], l[3], l[1], l[1]],
        '5': [l[3], l[0], l[3], l[1], l[3]],
        '6': [l[3], l[0], l[3], l[2], l[3]],
        '7': [l[3], l[1], l[1], l[1], l[1]],
        '8': [l[3], l[2], l[3], l[2], l[3]],
        '9': [l[3], l[2], l[3], l[1], l[3]],
        '0': [l[3], l[2], l[2], l[2], l[3]],
    }

    digits = digits.strip()

    for n in digits:
        if not n.isdigit():
            raise Exception('All input values must be an int')

    for i in range(0, 5):
        to_print = ''
        for n in digits: 
            to_print = to_print + digit_map[n][i] + ' '
        print(to_print)
        
if __name__ == '__main__':
    led_display()
