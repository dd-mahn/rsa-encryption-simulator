def decrypt(pk, ciphertext):
    # pk là khóa bí mật bao gồm key 'd' và modulus 'n'
    d, n = pk

    # Bản mã được giải mã từng kí tự một.
    # Với mỗi kí tự, ta thực hiện phương trình giải mã với d và n.
    # Sau đó chuyển kết quả về dạng kí tự sử dụng hàm chr.
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)