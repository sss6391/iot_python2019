names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
kim = lee = young = 0
list_names = names.split(',')
for name in names:
    if name[0] == '김':
        kim += 1
    if name[0] == '이':
        lee += 1
    if name == '이재영':
        young += 1
set_name = set(list_names)
list_names = list(set_name)
list_names.sort()
print(list_names)
print(kim)
print(lee)
print(young)


