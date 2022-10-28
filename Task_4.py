def encodeText(my_string):
    encoded = ''
    previous_symb = ''
    count = 1
    if not data:
        return ''
    for symb in my_string:
        if symb != previous_symb:
            if previous_symb:
                encoded += str(count) + previous_symb
            count = 1
            previous_symb = symb
        else:
            count += 1
    else:
        encoded += str(count) + previous_symb
        return encoded
def decodeText(my_string):
    decoded = ''
    count = ''
    for symb in my_string:
        if symb.isdigit():
            count += symb
        else:
            decoded += symb * int(count)
            count = ''
    return decoded
with open('Original_data.txt', 'r+') as data:
    xfile = data.readline()
xfile = encodeText(xfile)
xxfile = open("Encoded_data.txt", "w")
xxfile.write(xfile)
xxfile.close()
with open('Encoded_data.txt', 'r+') as data:
    xxxfile = data.readline()
xxxfile = decodeText(xxxfile)
xxxxfile = open("Decoded_data.txt", "w")
xxxxfile.write(xxxfile)
xxxxfile.close()
print('Процесс завершен. Данные помещены в соответствующие файлы.')