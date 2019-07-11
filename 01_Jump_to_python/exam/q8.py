file = open('abc.txt', 'r')
lines = file.readlines()
file.close()
save = []
for index in range(len(lines)-1,-1,-1):
    save.append(lines[index].rstrip())

str_save= str('\n'.join(save))
file = open('abc.txt', 'w')
file.write(str_save)
file.close()
