print('sinh vien: ho duc minh')
print('mssv:235752021610038')
print('##########')

input_file=open('example.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input_file.close()


