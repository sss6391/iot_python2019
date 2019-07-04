#coding: cp949

poket = ['종이', '핸드폰', '현금']

if '현금' or '신용카드' in poket 
#현급은 상수형 문자열 객체로서 값이 있기 때문에 무조건 Ture를 반환한다
#아래처럼 써야된다.
if '현금' in poket or '신용카드' in poket 
