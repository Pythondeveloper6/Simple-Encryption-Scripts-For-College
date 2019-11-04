'''
    simple script to encrypt and decrypt with substituation 
    developed by : Mahmoud Ahmed - pythondeveloper6@gmail.com

'''

from string import ascii_letters
cipher_letters = ''

class Main:
    def __init__(self):
        plaintext =  input('Please Enter Your Text :')
        global cipher_letters
        cipher_letters = input('Enter Cipher Text : ')
        self.Choice(plaintext)


    def Choice(self , plaintext ):
        user_choice = input('For Encryption Press E , and for Decryption Press D :  ')
        if user_choice == 'E' :
            self.Encrypt(plaintext )

        elif user_choice == 'D' :
            self.Decrypt(plaintext)


    def Encrypt(self , plaintext ):
        trans = str.maketrans(ascii_letters, cipher_letters)
        print(plaintext.translate(trans))

    def Decrypt(self ,plaintext):
        trans = str.maketrans(cipher_letters, ascii_letters)
        print(plaintext.translate(trans))



def main_app():
    app = Main()

if __name__ == '__main__':
    main_app()
