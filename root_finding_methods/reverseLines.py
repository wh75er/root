file1 = open("test1.txt", 'r+')
file2 = open("test2.txt", 'a')
k=0
for i in file1:
    k+=1
while k!=0:
    file1.seek(0)
    
    for i in file1:
        if i[-1:]!='\n':
            i+='\n'
        if i != s:
            last_line = i
        else:
            break
    s = last_line
    file2.write(last_line)
    k-=1

file1.close()
file2.close()
