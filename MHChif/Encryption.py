import random
from  math import gcd
import os

class Encryption:

    w = []
    q = 0
    r = 0
    b = []
    encrypted_text = []

    def __init__(self):
        self.generate_w()
        self.generate_q()
        self.generate_r()
        self.generate_b()

    # генератор возрастающего w
    def generate_w(self):
        for i in range(8):
            self.w.append( sum(self.w) + random.randint(1, 10) )
        print("w = ", self.w)

    # генерируем рандомное q с условием q > sum(w)
    def generate_q(self):
        num = sum(self.w)
        self.q = random.randint(num, num + 100)
        print("q = ", self.q)

    # генерация рандомного r взаимно простого с q
    def generate_r(self):
        while True:
            self.r = random.randint(1, self.q)
            if gcd(self.q, self.r) == 1:
                break
        print("r = ", self.r)

    # генерация b - открытого ключа
    def generate_b(self):
        self.b = [(wi * self.r) % self.q for wi in self.w]
        print("b = ", self.b)

    # читаем текст из консоли
    def read_user_input(self):
        user_input = input("Enter text for encryption: ")
        ascii_decimal = [ord(x) for x in user_input]
        ascii_binary = [bin(x)[2:].zfill(8) for x in ascii_decimal]
        self.encrypt(ascii_binary)

    # шифруем бинарные значения и печатаем
    def encrypt(self, ascii_binary):
        encrupted_text_chr=""
        for byte in ascii_binary:
            sum = 0
            for i, x in enumerate(byte):
                sum += int(x) * self.b[i]
            self.encrypted_text.append(sum)
            #чтобы вывести строку
            encrupted_text_chr+=chr(sum)
        print("Encrypted text:\n", encrupted_text_chr)