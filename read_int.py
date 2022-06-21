def read_int(prompt, min, max):
    try:
        x = input(prompt)
        x = int(x)
        min = int(min)
        max = int(max)
    except ValueError:
        print('Error: wrong input')
        return read_int("Enter a number from -10 to 10: ", -10, 10)
    try:
        assert min <= x <= max 
    except:
        print('Error: the value is not within permitted range ({}..{})'.format(min, max))
        return read_int("Enter a number from -10 to 10: ", -10, 10)
    
    return x
    
v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
