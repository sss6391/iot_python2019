import threading
import time
import  ctypes

g_Balcony_Windows = False
g_AI_Mode = False
schedule_cycle = 2

def terminate_ai_mode():
    if not ai_scheduler.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def update_scheduler():
    while True:
        time.sleep(schedule_cycle)
        print(f"\n스케줄러 작동..  {schedule_cycle}초 주기")

while True:
    print('\n메뉴를 선택하세요')
    print('1. 장비 상태 조회')
    print('2. 인공지능 모드 변경')
    print('3. 종료')

    menu_num = int(input('메뉴입력: '))
    if menu_num == 1:
        print('현재 발코니 창문 : ', end='')
        if g_Balcony_Windows == True: print('열림')
        else: print("닫힘")
    elif menu_num == 2:
        print('인공지능 모드: ',end='')
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode == True:
            ai_scheduler = threading.Thread(target=update_scheduler)
            ai_scheduler.daemon = True
            ai_scheduler.start()
            print("작동 완료!")
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except: pass
            print("정지 완료!")
    else: break