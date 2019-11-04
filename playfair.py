'''
    simple script to encrypt and decrypt with playfair
    developed by : Mahmoud Ahmed - pythondeveloper6@gmail.com

'''

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
        pass



    def Decrypt(self ,plaintext, key):
        pass


def main_app():
    app = Main()

if __name__ == '__main__':
    main_app()
