
f1 = open('111.txt','r')
f2 = open('result.txt', 'a')
k = 1

for line in f1:
    if k % 2 == 0:
        f2.write(line)
    k +=1

k = 1
f1.seek(0)
for line in f1:
    if k % 2 != 0:
        f2.write(line)
    k += 1

f1.close()
f2.close()
