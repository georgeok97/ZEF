import time
import random


codes = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]
a = ord('А')


def sss():
    for i in range(a, a + 32):
        time.sleep(0.3)
        sss = f'{chr(155)}{random.choice(codes)}m{chr(i)}'
        return sss

 sss()
print(sss, end=' ')
print('\x1b[0m')
