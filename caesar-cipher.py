'''
    simple script to encrypt and decrypt with caeser cipher
    developed by : Mahmoud Ahmed - pythondeveloper6@gmail.com

'''

Letter_to_index = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
Index_to_letters = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

class Main:
    def __init__(self):
        plaintext =  input('Please Enter Your Text :')
        key = int(input('Please Enter Your Key :'))
        self.Choice(plaintext , key)


    def Choice(self , plaintext , key):
        user_choice = input('For Encryption Press E , and for Decryption Press D :  ')
        if user_choice == 'E' :
            self.Encrypt(plaintext , key)

        elif user_choice == 'D' :
            self.Decrypt(plaintext, key)


    def Encrypt(self , plaintext , key):
        ciphertext = ""
        for c in plaintext.upper():
            if c.isalpha():
                ciphertext += Index_to_letters[ (Letter_to_index[c] + key)%26 ]
            else:
                ciphertext += c
        print(ciphertext)

    def Decrypt(self ,plaintext, key):
        plaintext2 = ""
        for c in plaintext.upper():
            if c.isalpha():
                plaintext2 += Index_to_letters[ (Letter_to_index[c] - key)%26 ]
            else:
                plaintext2 += c

        print(plaintext2)


def main_app():
    app = Main()

if __name__ == '__main__':
    main_app()
