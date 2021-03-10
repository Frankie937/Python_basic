# print("안녕")
# hobby= "산책"
# print(3==3)
# cabinet = {"A-3" : "유재석", "b-3":"김태호"}
# print(cabinet)
# print(cabinet.keys())
# print(cabinet.values())

#숫자처리함수
print(abs(-5))
print(round(3.67))
print(max(5,12,85))
from math import * #math 라는 라이브러리에서 불러온다는 의미 
print(floor(3.65)) #내림
print(ceil(3.14))  #올림
print(sqrt(16)) #제곱근

#랜덤함수
from random import *
print(random()) #0.0 ~ 1.0 미만의 임의의 값 출력
print(random()*10) #0.0 ~ 10.0미만의 임의의 값 출력 
print(int(random()*10)) #0 ~ 10 미만의 임임의 값(정수) 출력 
print(randrange(0,10)) #0 ~ 10 미만의 임의의 값(정수) 출력 

#로또 관련 코드 써보기 (1부터 45 이하의 임의의 값(정수) 출력)
print(int(random()*45)+1)
print(randrange(1,46))
print(randint(1,45)) # 양쪽 값 모두 포함

#퀴즈_2
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월"+str(date)+"일로 선정되었습니다.")

sentence= """나는 28세 여성입니다. 
안녕하세요 반갑습니다."""
print(sentence)

python = "Python is Amazing"
print(python.find("java")) # find 에서는 없는 값 찾을 때 '-1' 출력
#print(python.index("java")) # index에서는 없는 값 찾을 때 오류남

print("Reddd Apple\rPine")
print("Red\tApple")

#퀴즈_3
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1} 입니다." .format(url, password))

#퀴즈_4
from random import *
id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(id)
chicken = sample(id, 1)
id_b = set(id)-set(chicken)
id_c = list(id_b)
shuffle(id_c)
coffee = sample(id_c, 3)

print("""---당첨자 발표---
치킨 당첨자 : {0}
커피 당첨자 : {1}
--축하합니다--""" .format(chicken, coffee))


#퀴즈_4 정답(나도코딩)
users = range(1,21) #1부터 20까지 숫자 생성
#print(type(users)) #-> users 타입이 range로 나옴 
users = list(users)
shuffle(users)
winners = sample(users, 4)
print("""---당첨자 발표---
치킨 당첨자 : {0} 
커피 당첨자 : {1}
--축하합니다--""" .format(winners[0], winners[1:]))