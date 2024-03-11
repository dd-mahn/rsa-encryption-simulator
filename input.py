from is_prime import is_prime
from make_prime import make_prime


def paramInput():
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    
    if p == q:
        print("p and q cannot be the same value")
        return paramInput()
    
    if not (is_prime(p) and is_prime(q)):
        print("Both numbers must be prime.")
        print("Your number is being modified to be prime")
        print("Your first prime number: ",make_prime(p))
        print("Your second prime number: ",make_prime(q))
        
    return p, q