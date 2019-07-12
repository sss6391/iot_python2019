file = open('abc.txt', 'r')
lines = file.readlines()
file.close()

lines.reverse()

file = open('abc.txt', 'w')
for line in lines:
    line = line.rstrip()
    file.write(line)
    file.write('\n')
file.close()
