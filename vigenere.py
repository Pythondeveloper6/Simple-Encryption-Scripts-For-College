'''
    simple script to encrypt and decrypt with vigenere 
    developed by : Mahmoud Ahmed - pythondeveloper6@gmail.com

'''
class Main:
    def __init__(self):
        plaintext =  input('Please Enter Your Text :')
        key = input('Please Enter Your Key :')
        self.Choice(plaintext , key)


    def Choice(self , plaintext , key):
        user_choice = input('For Encryption Press E , and for Decryption Press D :  ')
        if user_choice == 'E' :
            self.Encrypt(plaintext , key)

        elif user_choice == 'D' :
            self.Decrypt(plaintext, key)

    def Encrypt(self ,plaintext, key):
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        print(ciphertext)

    def Decrypt(self ,ciphertext, key):
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        ciphertext_int = [ord(i) for i in ciphertext]
        plaintext = ''
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        print(plaintext)


def main_app():
    app = Main()

if __name__ == '__main__':
    main_app()
