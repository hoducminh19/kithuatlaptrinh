print('sinh vien: ho duc minh')
print('mssv:235752021610038')
print('##########')
chuoi = input("Nhập chuỗi: ")
chuoi_khong_chu_so = "".join([ky_tu for ky_tu in chuoi if not ky_tu.isdigit()])
print("Chuỗi sau khi loại bỏ chữ số:", chuoi_khong_chu_so)
