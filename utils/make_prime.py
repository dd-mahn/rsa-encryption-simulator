from is_prime import is_prime

def make_prime(a):
    while not is_prime(a):
        a += 1       
    return a
        