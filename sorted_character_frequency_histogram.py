from os import strerror

file_location = input('provide file path to read:')

char_dict = {}

try:
    for line in open(file_location, 'rt'):
        for ch in line:           
            if ch.isalpha():
                ch = ch.lower()
                if ch in char_dict:
                    char_dict[ch] += 1
                else:
                    char_dict[ch] = 1
    file.close()
except IOError as e:
    print('I/O error occured:', strerror(e.errno))
    exit(e.errno)

file_location = file_location.split('.')
file_location[-2] = file_location[-2] + '.hist'
file_location = '.'.join(file_location)
out_file = open(file_location, 'wt')
for i in sorted(char_dict, key = char_dict.get, reverse = True):
    line = i + ' -> ' + str(char_dict[i]) + '\n'
    out_file.write(line)
    
out_file.close()
