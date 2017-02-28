import pyipinfoio
f = open('ip.txt', 'r')
list = f.readlines()
list = [x.strip() for x in list]
for i in range(0, len(list)):
    k = open('ip-info.txt', 'a')
    ip = pyipinfoio.IPLookup()
    b = ip.lookup(list[i], 'country')
    c = ip.lookup(list[i], 'city')
    w = list[i] + ';' + 'country;' + b + 'city;' + c + '\n'
    k.write(w)
    k.close()
f.close()
