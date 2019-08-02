import re
mail_adress =  ['park@naver.com', 'kim@daum.net', 'lee@myhome.co.kr']

p = re.compile('.*[@].*[.](?=com$|net$).*$')

for mail in mail_adress:
    m = p.search(mail)
    print(m)

