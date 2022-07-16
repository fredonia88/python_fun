import os

def find(path, dir, matching_directories = []):
    for i in os.listdir(path):
        if i == '.DS_Store':
            continue
        else:
            if d == i:
                print('appending:', path + d)
                matching_directories.append(path + d)
            try:
                print('attempting recursive search at:', path + i + '/')
                find(path + i + '/', dir, matching_directories)
            except Exception as e:
                print(e.__str__())

    return matching_directories

p = '/Users/user.name/Desktop/tree/'
d = 'python'
directories = find(p, d)
print(directories)
