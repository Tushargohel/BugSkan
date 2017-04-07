import re
import os
b = input("enter the file name:")
a = int(input("enter the id"))
str1 = 'SecRule REQUEST_HEADERS:Referer "^https?://(www\.)?'
str2 = '/?"  "phase:1,log,deny,id:'
str3 = ',status:503,msg:\'referer spam\'"\n'
with open(b) as file:
    lines = file.readlines()

lines = [i.replace('\n','') for i in lines]
for i in range(len(lines)):
    lines[i] = re.escape(lines[i])
    a = a + 1
    rule = str1+lines[i]+str2+ str(a)+str3
    print(rule)
    Rule = open("/usr/share/bugskan-crs/Bugskan_rules.conf", "a")
    Rule.write(rule+"\n")

os.system("service apache2 restrat")