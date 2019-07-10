class MyError(Exception):
    def __str__(self):
        return "Not allowed Nickname"

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
    print("핵심로직")
except MyError as e:
    print(e)
    print("허용되지 않는 별명입니다")
