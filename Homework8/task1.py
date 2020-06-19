"""
Написать функцию `XOR_cipher`, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
возвращает строку, зашифрованную путем применения операции XOR (битовое исключающее ИЛИ) над символами строки с ключом.
Написать также функцию `XOR_uncipher`, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""


key = 'asdfln3j34tnonfdkjnflksdfnla'
code = 'this is my message'


def xor_cipher(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])


encoded = xor_cipher(code, key)
print(encoded)


decoded = xor_cipher(encoded, key)
print(decoded)

