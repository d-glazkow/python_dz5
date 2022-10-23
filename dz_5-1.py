#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

lst = ['jgkj','knkn','lkku','kjgku','ljhgg','assd','jhkgglg']
harf1 = 'k'
harf2 = 'l'
a = len(lst)
print(a)
print(lst)
for i in range(a-1):
    string = lst[i]
    if string.find(harf1) >= 0:
        if string.find(harf2) >= 0:
            lst.pop(i)
print(lst)
