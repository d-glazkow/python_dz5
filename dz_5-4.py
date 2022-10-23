#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(text):
    encoded_str = ""
    i = 0
    while i <= len(text)-1:
        count = 1
        ch = text [i]
        j = i
        while j < len(text)-1:
            if text [j] == text [j+1]:
                count = count +1
                j = j + 1
            else:
                break
        encoded_str = encoded_str + str(count) + ch
        i = j + 1
    return encoded_str
def decode(RLE_text):
    decoded_text=""
    i = 0
    j = 0
    while i <= len(RLE_text)-1:
        count = int(RLE_text[i])
        ch = RLE_text[i+1] 
        for j in range(count):
            decoded_text = decoded_text + ch
            j = j + 1
        i = i + 2
    return decoded_text

text = input('введите текст для кодировки:\n')
RLE_text = encode(text)
back_to_text = decode(RLE_text)

print('сжатие :',{RLE_text})
print("восстановление :", {back_to_text})
