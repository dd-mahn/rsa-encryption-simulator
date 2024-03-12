import random

from sympy import mod_inverse
from utils.gcd import gcd

def generate_keypair(p, q):
    print("Generating your public/private keypairs now . . .")
    # Tính n
    n = p * q

    # Tính hàm Euler
    phi = (p-1) * (q-1)

    # Chọn số nguyên e sao cho e và phi(n) là hai số nguyên tố cùng nhau
    e = random.randrange(1, phi)

    # Đảm bảo e và phi(n) có ước chung lớn nhất bằng 1
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Sử dụng thuật toán Euclid mở rộng để tạo khóa bí mật
    d = mod_inverse(e, phi)

    # Trả về bộ khóa công khai (e,n) và khóa bí mật (d,n)
    return ((e, n), (d, n))
