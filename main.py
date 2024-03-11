from utils.is_prime import is_prime
from utils.decrypt import decrypt
from utils.encrypt import encrypt
from utils.generate_keypair import generate_keypair
from utils.make_prime import make_prime
from flask import Flask, request, render_template

app = Flask(__name__)
app.template_folder = 'templates'
app.static_folder = 'static'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        all_prime = True
        p = int(request.form.get('p'))
        q = int(request.form.get('q'))
        message = request.form.get('message')
        
        if is_prime(p) and is_prime(q): 
            all_prime = True
        else: 
            all_prime = False
            p = make_prime(p)
            q = make_prime(q)
        
        public, private = generate_keypair(p, q)
        
        encrypted_msg = encrypt(public, message)
        
        decrypted_msg = decrypt(private, encrypted_msg)
        
        return render_template('index.html',all_prime=all_prime, public_key=public, private_key=private, encrypted_msg=encrypted_msg, decrypted_msg=decrypted_msg, primeP=p, primeQ=q, message = message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    
    
# Terminal version:
# from utils.input import paramInput
# if __name__ == '__main__':
#     p, q = paramInput()
#     public, private = generate_keypair(p, q)
#     print("Your public key is ", public ," and your private key is ", private)
#     number = input("Enter a number to encrypt with your public key: ")
#     print(number)
#     encrypted_msg = encrypt(public, number)
#     print("Your encrypted message is: ")
#     print(''.join(map(lambda x: str(x), encrypted_msg)))
#     print("Decrypting message with private key ", private ," . . .")
#     print("Your message is:")
#     print(decrypt(private, encrypted_msg))
