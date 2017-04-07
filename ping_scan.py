import os


def nmap(opt, ip):
    a = []
    com = "nmap " + opt + " " + ip
    proc = os.popen(com)
    r = str(proc.read())
    l = r.splitlines()
    for i in range(len(l)):
        m = l[i].find('report for')
        if(m == 10):
            a.append((l[i][m + 11:m + 22]))

    return a


a = input("enter ip:")
b = input("enter scan type:")
print(nmap(b, a))
