def digit_of_life(
    bday = input('Enter your birthday in YYYYMMDD, YYYYDDMM or MMDDYYYY format: ')
):
    '''
    takes date of your birthday in 8 digit format and returns digit of life
    :param bday: date of your birthday
    '''

    try:
        test_bday = int(bday)
    except:
        raise Exception('All birthday digits must be numeric')

    if test_bday < 1:
        raise Exception('Birthday must be a positive number')

    while len(bday) > 1:
        bday_number = sum([int(n) for n in bday])
        if bday_number < 10:
            print('Your digit of life is:', bday_number)
            break
        else:
            bday = str(bday_number)
            
if __name__ == '__main__':
    digit_of_life()
