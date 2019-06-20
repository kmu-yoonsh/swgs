# 입력값: 년도, 월, 일
# 출력값: 요일

# 전제: 1년 1월 1일은 월요일

# 1. 1년 1월 1일부터 입력된 년 월 일까지의 모든 일자를 더하자

# 1.1 년도에 따른 날짜 더하기 (1년부터 입력받은 년도 직전 년도까지)
# 윤년 주의하기: 윤년이면 1년은 366일, 평년이면 1년은 365일

# 1.2 월에 따른 날짜 더하기 (1월부터 입력받은 직전 월까지)
# 31일(1, 3, 5, 7, 8, 10, 12월), 30일(4, 6, 9, 11월), 28일(평년 2월), 29일 (윤년 2월)

# 1.3 일애 따른 날짜 더하기

# 2. 총 일자를 7로 나눈 나머지 값에 의해 요일을 출력
# 0: 월요일, 1: 화요일, 2: 수요일, 3: 목요일, 4: 금요일, 5: 토요일, 6: 일요일

year    = int(input("Input Year : "))
month   = int(input("Input Month : "))
date    = int(input("Input Date : "))

sum_date = int(0)
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daysMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, year):
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
        sum_date += 366
    else:
        sum_date += 365

for i in range(1, month):
    sum_date += daysMonth[i - 1]
    if i == 2 and i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
        sum_date += 1

sum_date += date

print("%04d" % year, "%02d" % month, "%02d" % date, "is", day[(sum_date % 7) - 1])
# 파이썬은 포문 내의 if를 포문이 끝나고 else가 수행되도록 할 수 있다.
