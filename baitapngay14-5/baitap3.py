# a có chia hết cho cho chữ số b nhỏ nhất không
a = int(input("Nhập a: "))
b = input("Nhập b: ")

nho_nhat = int(min(b))

if nho_nhat != 0 and a % nho_nhat == 0:
    print("Chia hết")
else:
    print("Không chia hết")