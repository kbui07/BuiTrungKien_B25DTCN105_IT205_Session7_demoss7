name = 'Hiếu 6 đẹp trai'
print(f'Chữ cái đầu tiên trong biến name: {name[0]}')

# lấy 3 kí tự cuối
print(name[-3:])

for i in range(0, 5, 1):
    print(name[i], end = '')

# slicing: cắt chuỗi
print(f'\n{name[0:5:2]}')

# đảo ngược chuỗi
print(name[::-1])

# nối chuỗi
status_user = 'lười học'
full_status_user = name + " " + status_user
print(full_status_user)

# nhân bản chuỗi dùng toán tử *
print((status_user + " ") * 3)

# toán tử in: kiểm tra có tồn tại chuỗi trong chuỗi hay không
full_name = 'Hiếu đẳng cấp'
validate = 'Cấp'
is_true = validate in full_name
print(is_true)

# tìm xem full_name có chữ 'cấp' hay không
# tìm chỉ số index của chữ cấp trong full_name
find_index = full_name.find('cấp')
print(find_index)

full_name_new = full_name.replace('đẳng cấp', 'phèn')
print(full_name_new)

print('    '.join(full_name.split(' ')))

