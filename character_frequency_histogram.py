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
    
print('alpha counts in file:')
for i in char_dict:
    print(i + ' ->', char_dict[i])
