# # словари
# # кортеж это ()
# # список он изменяемый а кортеж менять нельзя
# d = {} #пустой словарь
# d['botinok'] ='  что за тяги бархатные' #
# d['botsinok'] ='  что за тяги лютые'
# print(d)
#
# d1 = {
#     'bashmak': 'adidas',
#     'bashmak1': 'dc',
#     'bashmak2': 'qicksilver',
#     'bashmak3': 'nike',
#     5: 'пять',
# }
# print(d1['bashmak'])
# # l = [4 , 2, 7]
# # del l [1] # удаление по индексу
# # print(l)
# print(d1['bashmak'])
# for key in d1: # перебор ключей
#     print(key)
#
# for v in d1.values(): #  перебор значений
#     print(v)
# for key, val in d1.items(): # (ключ , значение)
#     print(('[ключ]:', key,'[значение]:',val))
# d1= {
#     'bash': 'nike',
#     5: 'five'
# s = set()
# s1 = {'a','b','c','d'}
# print(s1)
#
# s1 = {'a','b','c','d'}
#
# if len(s1) != len(s2):
#     print(True)
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
print(s1.union(s2))

print(s1 | s2)# то же самое что и s1.union(s2)
print(s1 & s2) #.intersection()
print(s1 - s2) #.difference()
print(s1^ s2)# .summetric_difference()



