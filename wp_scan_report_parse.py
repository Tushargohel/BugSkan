import os
a = 'ruby wpscan.rb --url '
b = input("enter domain name")
c = '--user-agent kaushal  --log >'
d = b.split('.')[0] + '.txt'
os.system(a + b + c + d)
list = []
with open(d, 'r') as f:
    for i in f:
        if '[!] Title:' in i:
            list.append(i)
for i in range(0, len(list)):
    tmp = list[i]
    print(tmp.split('[!] Title:')[1])
f.close()
