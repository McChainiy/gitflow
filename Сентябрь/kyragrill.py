f = open('prices.txt', 'r').readlines()
totalprice = 0
for i in f:
    i = i.split('\t')
    totalprice += int(i[1]) * float(i[2])
totalprice = str(totalprice).split('.')
if len(totalprice) == 1:
    print(0)
elif len(totalprice[1]) == 1:
    print(totalprice[0], totalprice[1] + '0', sep='.')
else:
    print(totalprice[0], totalprice[1][:2], sep='.')
