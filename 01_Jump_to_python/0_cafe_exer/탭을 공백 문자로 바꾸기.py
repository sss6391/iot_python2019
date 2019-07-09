with open("code.txt", 'r') as file:
    lines = file.read()
    lines_repleaced = lines.replace('\t',' ')

with open("code.txt", 'w') as file:
    file.write(lines_repleaced)
