def encrypt(pk, plaintext):
    # pk là khóa công khai bao gồm key 'e' và modulus 'n'
    e, n = pk

    # Bản rõ sẽ được mã hóa từng kí tự 1.
    # Với mỗi kí tự, chuyển thành dạng ASCII sử dụng hàm ord.
    # Sau đó tính phương trình mã hóa.
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher