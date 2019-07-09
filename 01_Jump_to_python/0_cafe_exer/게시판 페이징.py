input_m = int(input("총 건수를 입력하세요: "))
input_n = int(input("총 페이지 수를 입력하세요: "))
print_result = 0
if input_m == 0:
    print_result = 0
elif input_m == 1 & input_n == 1:
    print_result = 1
else: print_result = int(input_m / input_n)

print("출력: %d" % print_result)
