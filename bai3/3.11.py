print('sinh vien: ho duc minh')
print('mssv:235752021610038')
print('##########')
def benefit(t, n, k):
    t_decimal = t / 100
    total_amount = n * (1 + t_decimal) ** k
    return round(total_amount, 2)
try:
    t = float(input("Nhập lãi suất (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))
    print(f"Số tiền nhận được sau {k} tháng: {benefit(t, n, k)}")
except ValueError:
    print("Vui lòng nhập các giá trị hợp lệ.")
