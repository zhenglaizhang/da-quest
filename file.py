file_name = "./cn.txt"

file_obj = open(file_name, 'r', encoding='utf-8')

# read line by line
print(file_obj.readline())

# read all
all_content = file_obj.read()

print(all_content)

# close file handler
file_obj.close()

with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        print('{}=> {}'.format(i, line))

lines = ['this is line %i\n' % n for n in range(100)]
with open('/tmp/out', 'w', encoding='utf-8') as file:
    file.writelines(lines)
