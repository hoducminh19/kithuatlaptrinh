print('sinh vien: ho duc minh')
print('mssv:235752021610038')
print('##########')
cac_so_chan=[]
for number in range(1000,3000):
    if number%2 == 0 and all((int(digit)) % 2 == 0 for digit in str(number)):
        cac_so_chan.append(str(number))
print(','.join(cac_so_chan))
