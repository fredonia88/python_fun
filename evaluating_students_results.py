file_path = input('provide file path:')
file = [line for line in open(file_path, 'rt')]

if len(file) == 0:
    raise FileEmpty('file is empty')

student_scores = {}

for line in file:
    line = line.split()
    if len(line) != 3:
        raise BadLine('must have 3 words per line. line has {} words'.format(len(line)))
    line[2] = float(line[2])
    if line[0] + '_' + line[1] not in student_scores:
        student_scores[line[0] + '_' + line[1]] = line[2]
    else:
        student_scores[line[0] + '_' + line[1]] += line[2]
        
for student in student_scores:
    student_name = student.split('_')
    print(student_name[0], student_name[1], student_scores[student])
