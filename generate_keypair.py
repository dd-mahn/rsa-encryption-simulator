import random

from sympy import mod_inverse
from gcd import gcd
from is_prime import is_prime


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Cả hai số phải là số nguyên tố.')
    elif p == q:
        raise ValueError('Hai số không được trùng nhau')
    # Tính n
    n = p * q

    # Tính hàm Euler
    phi = (p-1) * (q-1)

    # Chọn số nguyên e sao cho e và phi(n) là hai số nguyên tố cùng nhau
    e = random.randrange(1, phi)

    # Đảm bảo e và phi(n) có ước chung bằng 1
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Sử dụng thuật toán Euclid mở rộng để tạo khóa bí mật
    d = mod_inverse(e, phi)

    # Trả về bộ khóa công khai và khóa bí mật
    return ((e, n), (d, n))
