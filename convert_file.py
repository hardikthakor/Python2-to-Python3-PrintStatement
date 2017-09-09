import os
import re

start = " ("
end = ")"


print ("Enter Directory Path : ", end="")
base_dir = input()

html_files = []

for root, _, files in os.walk(os.path.normpath(base_dir)):
    for f in files:
        if f.endswith('.py'):
            html_files.append(os.path.join(root, f))


for html_file in html_files:
    with open(html_file, 'r') as f:
        data = f.read()
    arr = list(map(str, data.split("\n")))
    data_list = []
    final = []
    a = ''
    for letter in range(len(arr)):
        regex = r'(print)( )"(.+?)"'
        changes = re.findall(regex, arr[letter])
        if not changes:
            final.append(arr[letter])
        elif changes[0][0] == 'print':
            a = arr[letter]
            test = list(map(str, a.split(" ")))
            test.insert(1, start)
            test.append(end)
            a = ''.join(test)
        final.append(a +'\n')
        a = ''
    a = ''.join(final)
    with open(html_file, 'w') as f:
            f.write(a)