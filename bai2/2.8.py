print('sinh vien: ho duc minh')
print('mssv:235752021610038')
print('##########')
a, b = 1, 2
total = 0
print(a,end=" ")
while (a <=4000000-1):
    if a % 2 == 0:
        total += a
    a, b = b, a+b
    print(a,end=" ")
print("\n sum of prime numbers term in fibonacci series: ",total)