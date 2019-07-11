a = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"

mos = {'.-': 'A', '-...': 'B','-.-.': 'C', '-..': 'D','.': 'E', '..-.':'F', '--.':'G',
       '....':'H', '..':'I',  '.---': 'J', '-.-':'K', '.-..':'L','--':'M', '-.':'N',
       '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T','..-': 'U',
       '...-':'V','.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z'}

input_str = input("모스 부호 입력: ").split(' ')
result = []
for match in input_str:
    if match == '':
        result.append(' ')
        continue
    result.append(mos[match])
result =''.join(result)
print(result)
