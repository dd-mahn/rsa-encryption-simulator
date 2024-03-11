from utils.decrypt import decrypt
from utils.encrypt import encrypt
from utils.generate_keypair import generate_keypair
from utils.input import paramInput

if __name__ == '__main__':
    p, q = paramInput()
    public, private = generate_keypair(p, q)
    print("Your public key is ", public ," and your private key is ", private)
    number = input("Enter a number to encrypt with your public key: ")
    print(number)
    encrypted_msg = encrypt(public, number)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with private key ", private ," . . .")
    print("Your message is:")
    print(decrypt(private, encrypted_msg))
