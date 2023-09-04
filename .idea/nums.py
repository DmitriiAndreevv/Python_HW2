# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex
# используйте для проверки своего результата.

def sixteenformula(num):
    hex_string = "dmitrtii123456"
    hex_str = " "
    while num > 0:
        hex_str = hex_string[num % 16] + hex_str
        num // 16
        return hex_str


num = 356

hex_str = sixteenformula(num)
print(f"{num} = {hex_str}")
print(hex(num))
