import time
import random
from datetime import datetime

def showthescore():
    pass

def select_level():
    print("게임을 시작합니다")
    while True:
        level = input("숫자를 입력하여 레벨을 선택해 주세요 1. 쉬움 2. 보통 3. 어려움: ")
        if level == '1':
            return random.randint(1,1000)
            break
        elif level == '2':
            return random.randint(1,10000)
        elif level == '3':
            return random.randint(1,100000)
        else:
            print("1~3 숫자를 입력해주세요")

def game_start(right_answer):
    right_answer = str(right_answer)
    while True:
        input_numbers = input("숫자를 입력해주세요")

        pass


while True:
    start = int(input('1 입력시 시작 합니다. '))
    time.sleep(2)
    if start == 1:
        start_number = select_level()
        game_start(start_number)
        break
    showthescore()