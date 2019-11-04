'''
    simple script to encrypt and decrypt with row transpostions
    developed by : Mahmoud Ahmed - pythondeveloper6@gmail.com

'''

import math
class Main:
    def __init__(self):
        plaintext =  input('Please Enter Your Text :')
        key = input('Please Enter Your Key :')
        row = self.Create_matrix(key)
        self.Choice(plaintext ,row  , key)



    def Create_matrix(self , key):
        numbers = []
        for n in key :
            numbers.append(n)
        row_number = max(numbers)
        return row_number


    def Choice(self , plaintext , row , key):
        user_choice = input('For Encryption Press E , and for Decryption Press D :  ')
        if user_choice == 'E' :
            self.Encrypt(plaintext , row , key)

        elif user_choice == 'D' :
            self.Decrypt(plaintext)


    def Encrypt(self , plaintext , row , key):
        text = plaintext.replace(" " , "")
        text_length = len(text)
        row_cout = math.ceil(text_length/int(row))

        if text_length < int(row*row_cout) :
            rest  = (int(row)*int(row_cout)) - int(text_length)
            rest_of_text = list(range(rest))


        cipher_text = []

        for c in text :
            cipher_text.append(c)

        for n in rest_of_text :
            cipher_text.append('z')

        print(cipher_text)

        matrix = [[[] for i in range(int(row))] for c in range(row_cout)]

        for i ,l in enumerate(matrix) :
            for sl in l :
                sl = cipher_text[i]


        print(matrix)




    def Decrypt(self ,plaintext):
        pass


def main_app():
    app = Main()

if __name__ == '__main__':
    main_app()
