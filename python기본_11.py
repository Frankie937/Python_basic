# #**11-1 모듈(쉽게 설명하면, 필요한 것끼리 부품처럼 만들어진 파일이라고 보면 됨.
# # 예를 들어, 자동차를 타다가 타이어가 마모가 되면 타이어만 교체하면 되는 것 처럼 
# # 소프트웨어도 부품만 교체하거나 추가할 수 있게 만들면 유지보수도 쉽고, 코드의 재사용도 수월해지는 장점이 있음
# # 이런식으로 딱 필요한 것들끼리 부품처럼 잘 만드는 것을 '모듈화'라고 함
# # 파이썬에서는 함수 정의나 클래스 등의 파이썬 문장들을 담고 있는 파일을 모듈이라고 함 모듈은 확장자가 '.py'임)
# # 모듈은 내가 그 모듈을 쓰려는 파일과 같은 경로에 있거나 혹은 파이썬 라이브러리들이 모여있는 폴더에 있어야 사용 가능함! 

# # # 방법1
# # import theater_module
# # theater_module.price(3) 
# # theater_module.price_morning(4)
# # theater_module.price_soldier(5)
# # 방법2
# import theater_module as mv # 모듈명이 길 때, as를 활용
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)
# # 방법3
# from theater_module import * # 이렇게 쓰면, 모듈 내의 함수를 바로 호출 가능
# price(3)
# price_morning(4)
# price_soldier(5)
# # 방법4
# from theater_module import price, price_morning # 필요한 함수만 불러올 수 있음
# price(3)
# price_morning(4)
# # 방법5
# from theater_module import price_soldier as price # 불러온 함수에도 as 활용가능
# price(5)

# #**11-2 패키지(모듈들을 모아놓은 집합)
# # 하나의 디렉토리에 여러 모듈 파일들을 갖다 놓은 것을 패키지라고 쉽게 이해하면 됨
# import travel.thailand # 주의할 점: import를 쓸 때 맨뒤에는 모듈이나 패키지만 가능! (클래스나 함수는 import를 직접 바로 할 수 없음!)
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
# # from  import 구문에서는 모듈, 패키지, 클래스, 함수 모두 import 할 수 있음! 
# from travel.thailand import ThailandPackage 
# trip_to = ThailandPackage()
# trip_to.detail()
# from travel import vietnam 
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# #**11-3 __all__
# from travel import *
# trip_to = vietnam.VietnamPackage() # -> 오류 발생!! (__init__파일에 아무것도 없을 시)
# # travel 폴더 안에 __init__파일에 __all__ =[ ]을 정의해주지 않고 from travel import * 을 하게 되면 오류 발생 
# # 그 이유는, import *은 travel 패키지 않에 모든 것을 갖고오겠다는 것인데 실제 사용할 때에는 개발자가 그 공개 범위를 설정해줘야 함! 
# # 패키지 안에 포함된 것들 중에서 import되기 원하는 것만 공개하고 원하지 않는 것을 비공개로 설정할 수 있다는 의미

# #**11-4 모듈직접실행
# # 실제로 패키지나 모듈을 만들 때, 잘 동작하는지 테스트를 해봐야 함(if __name__ == "__main__" 구문 활용)
# # 모듈 내에서 실행되는 건지 외부에서 가져와서 실행하는 건지 구분해서 필요한 코드를 작성할 수 있음
# # thailand 모듈에 예제 있음(줄 5번 부터 11번까지)

# #**11-5 패키지, 모듈 위치 확인 방법 
# import inspect 
# import random
# print(inspect.getfile(random)) # 랜덤이라는 모듈이 어느 위치에 있는지 파일 정보를 알려주는 것
# from travel import *
# print(inspect.getfile(thailand))

# #**11-6 pip install (pip로 패키지 설치하기)
# # 지금 이미 수많은 패키지들이 존재하고, 지금도 누군가가 패키지를 새롭게 개발하고 있음 
# # 그러므로, 파이썬은 새로운 코드를 무조건 다 작성하는 것보다 이미 잘 만들어진 패키지를 필요한 곳에 가져다 쓰는 것도 굉장히 중요함!!
# # pypi 검색(구글링) https://pypi.org/
# # beautifulsoup4 검색(웹스크래핑에 대한 유명한 패키지)
# # <terminal 에 작성하는 부분>
# # pip install beautifulsoup4 -> beautifulsoup4 패키지가 설치됨 
# # pip list -> 현재 설치되어 있는 패키지들이 어떤 것이 있는 지 볼 수 있음
# # pip show beautifulsoup4 -> beautifulsoup4 패키지에 대한 정보를 알려줌
# # pip install --upgrade beautifulsoup4 -> 설치되어있는 패키지가 새로운 버전이 나와서 업그레이드가 필요할 때 
# # pip uninstall beautifulsoup4 -> 패키지 삭제할 때 

# #**11-7 내장함수(내장되어 있기 때문에 따로 import 할 필요 없이 바로 사용가능한 함수) 
# # input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다.!".format(language))
# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시 
# print(dir())
# import random # 외장 함수
# print(dir()) # random이 추가되어 있음
# import pickle
# print(dir()) random, pickle이 추가되어 있음
# print(dir(random)) # random 모듈 내에서 쓸 수 있는 모든 것들이 나옴
# # 내장함수-list 
# lst = [1, 2, 3]
# print(dir(lst)) # list 함수 내에서 쓸 수 있는 모든 것들이 나옴
# # 내장함수-문자열 str 함수 
# name = "Jim" # 문자열 함수 내에서 쓸 수 있는 모든 것들이 나옴 
# print(dir(name))
# # 더 많은 내장함수를 찾으려면, 
# # 구글에 'list of python builtins'로 검색하면 'https://docs.python.org/ko/3/library/functions.html'사이트 클릭해서 확인하면 됨 

# #**11-8 외장함수(직접 import 해서 사용해야 하는 함수)
# # 구글에 'list of python modules'로 검색하면 'https://docs.python.org/3/py-modindex.html' 외장함수 목록 확인 가능
# # glob : 경로 내의 폴더/ 파일 목록 조회 (윈도우 dir 과 똑같음)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일에 대해서 알려줘라는 것
# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리를 표시해달라는 의미
# folder = "sample_dir"
# if os.path.exists(folder): # sample_dir라는 폴더가 있으면 이 구문을 타라는 것
#     print("이지 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else: 
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다." )
# print(os.listdir()) # os.listdir ->glob과 비슷하게 쓸 수 있음
# # time : 시간 관련 함수들을 제공하는 외장함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# # timedelta : 두 날짜 사이의 간격 
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후

# # 퀴즈 10
# # --내가 한 것--
# import byme
# byme.sign("김민서", "3mins2@naver.com")

# # --나도코딩--
# import byme
# byme.sign()
