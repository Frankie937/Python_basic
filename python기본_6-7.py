# # if문 (굉장히 많이 쓰임)
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요 없어요치")

# temp = int(input("오늘 기온은 어때요?"))
# if 30 <= temp: 
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("쌀쌀하니 외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요.")

# # for(반복문)
# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}" .format(waiting_no))
# for waiting_no in range(5): #또는 range(0,5) 해도 똑같은 값(0~4까지_5직전) 나옴 
#     print("대기번호 : {0}" .format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠그루트"]
# for customer in starbucks:
#     print ("{0}, 커피가 준비되었습니다.".format(customer))

# # while(반복문) while 뒤에 오는 조건이 성립될 때까지 반복함 
# customer = "토르"
# index = 5
# while index >=1: 
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("폐기처분되었습니다.")
# # 무한루프에 빠지는 경우 -> ctrl+C 누르면 강제 종료됨 ! 
# # customer2 ="아이언맨"
# # index = 1
# # while True:
# #    print("{0}, 커피가 준비되었습니다. 호출: {1}회".format(customer2, index))
# #    index += 1

##퀴즈 5

# from random import *
# cnt = 0 # 총 탑승승객 수 
# for customer in range(1,51): # 1 ~ 50 이라는 수 (승객)
#     time = randrange(5,51) # 5분 ~ 50분 소요시간
#     if 5<= time <=15: # 5분~ 15분 이내의 손님(매칭성공), 탑승 승객 수 증가 처리
#         print("[O] {0}번째 손님 (소요시간 : {1}분".format(customer, time))
#         cnt += 1
#     else: # 매칭 실패한 경우
#         print("[ ] {0}번째 손님 (소요시간 : {1}분".format(customer, time))
    
# print("총 탑승 승객: {0} 분" .format(cnt))

# #7. 함수 (7-2 전달값, 반환값 )
# def deposit(balance, money): # 입금 
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance, money): #출금
#     if balance >= money: #잔액이 출금보다 많으면 
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100
#     return commission, balance-money-commission

# balance = 0
# balance = deposit(balance, 2000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원 이고, 잔액은 {1}원 입니다.".format(commission, balance))

# #7-3 기본값 
# def profile(name, age, main_lang) :
#     print("이름: {0}\t나이: {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang)) # 코드가 길면 \+엔터누르면 줄바꿈이 됨(같은 줄이라는 의미는 있으면서)

# profile("유재석", 20, "파이썬")
# profile("김태호",25, "자바")

# #만약 유재석, 김태호가 같은나이이고, 같은 언어이면 계속 반복적으로 적을 필요 없음
# #그러므로, 기본값을 넣어줌 
# def profile(name, age=17, main_lang="파이썬"):
#      print("이름: {0}\t나이: {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# #7-4 키워드값으로 함수 호출 가능 
# def profile(name, age, main_lang) :
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

# #7-5 가변인자
# def profile(name, age, *language): # *language 같은 변수가 가변인자(서로 다른 갯수의 값을 넣어줄 때 유용)
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")

# #7-6 지역변수와 전역변수
# #지역변수: 함수 내에서 쓸 수 있는 것(함수 호출될 때 만들어졌다가 호출이 끝나면 사라지는 것)
# #전역변수: 모든 공간에서 프로그램 내에서 어디서든지 부를 수 있는 함수 
# #일반적으로 전역변수 많이 쓰면 코드관리도 어려워지기 때문에 권장되는 방법은 아님 

# # 지역변수 
# gun = 10
# def checkpoint(soldiers): # 경계근무나가는 군인
#     gun = 20
#     gun = gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun)) # 10이 나옴 
# checkpoint(2) # 18이 나옴
# print("남은 총 : {0}".format(gun)) # 10이 나옴 

# # '전역변수'를 이용하면 다르게 나옴-'global' 이용! 
# gun = 10
# def checkpoint(soldiers): # 경계근무나가는 군인
#     global gun # 전역공간에 있는 gun 사용 (즉, 함수 밖에있는 'gun=10'이라는 변수를 'checkpoint'함수 내에서 쓰겠다는 의미!)
#     gun = gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun)) # 10이 나옴
# checkpoint(2) # 8이 나옴
# print("남은 총 : {0}".format(gun)) # 8이 나옴
# 그러나 일반적으로 전역변수를 많이 쓰면 코드가 어려워져서.. 가급적이면 함수의 전달값으로 던져서 계산하고 반환값을 받아서 사용함! 
# #(일반적임)전달값으로 던져서 계산하고 반환값으로 받아서 사용하는 방법 
# gun = 10  
# def checkpoint_ret(gun, soldiers):
#     gun = gun-soldiers 
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun 

# print("전체 총 : {0}".format(gun)) # 10이 나옴
# gun = checkpoint_ret(gun,2) # 8이 나옴 
# print("남은 총 : {0}".format(gun)) # 8이 나옴 

# #퀴즈 6 
# #--내가 푼 것 --
# def std_weight(height, gender) : 
#     if gender  == "male":
#         print ("키 {0}cm 남자의 표준 체중은 {1} kg 입니다.".format(height*100, round(height*height*22, 2))) 
#     else:
#         print("키 {0}cm 여자의 표준 체중은 {1} kg 입니다.".format(height*100, round(height*height*21, 2)))
# std_weight(1.75, "male")

# #--나도코딩 정답--
# def std_weight(height, gender): # 키 m 단위(실수), 성별 "남자"/"여자"
#     if gender == "남자":
#         return height*height*22
#     else:
#         return height*height*21
# height = 175 # cm 단위 
# gender = "남자"
# weight = round(std_weight(height/100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight)) 
