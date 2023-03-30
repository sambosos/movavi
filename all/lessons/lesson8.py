# # ======== запись в txt =======
# f = open('file.txt','w', encoding='utf-8') #na zapis
# f.write('ok\nok2')# na zapis v file
# f.close()
# # ========= чтение txt======
# f = open('file.txt','r', encoding='utf-8') #na zapis
# content = f.read() #чтение из файла
# print(content)
# f.close()
import json

# #=============================================
# try:
#     f = open('fu.txt','r', encoding='utf-8') #na zapis
# except FileNotFoundError:
#     print('not today  bruh.')
# else:
#     content = f.readlines()  # чтение из файла
#     print(content)
#     f.close()
#     print(content)
#     summa = 0
#     for number in content:
# #         summa = summa + int(number)
# #     print(summa)
# f = open('file.txt','r', encoding='utf-8') #na zapis
# content = f.read() #чтение из файла
# f.close()
# print(content)
# chisla = content.split() #раскалываем по пробелу
# print(chisla)
import json
data = [True, None, (1, 5), {1: "Значение"}, 'Eng']
f = open('file.json', 'w', encoding='utf-8') # на запись
# print(json.dumps(data, ensure_ascii=False))
json.dump(data, f, ensure_ascii=False) # выгрузить в жсон + записывает
# f.write('[1, 0.5, true]') # так тупо делать
# f.close()


f.close()