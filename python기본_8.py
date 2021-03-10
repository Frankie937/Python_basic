# #**8-1표준 입출력
# print("Python","Java") # Python Java 출력
# print("Python"+"Java") # PythonJava 출력
# print("Python","Java",sep=",") # Python,Java 출력
# print("Python","Java",sep=" vs ") # Python vs Java 출력
# import sys
# print("Python","Java", file=sys.stdout) # 보이는 결과는 차이없어보이지만, stdout은 표준출력으로 찍히는 것이고, stderr은 표준에러로 처리되는 것
# print("Python","Java", file=sys.stderr) # 즉, stdout은 크게 신경쓸 필요 없는데 stderr는 확인을 해서 프로그램 코드를 수정하든지 해야 되는 것 
# # 시험성적 출력 
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # 보기좋게 왼쪽 정렬, 오른쪽정렬(괄호숫자는 공간확보길이)
# # 은행 대기순번표처럼 출력-001, 002, 003... 같이 나타내려면 'zfill' 함수 활용!
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))
# # 표준 입력 
# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer)) # <calss 'str'> 이라고 나옴! 즉, input(사용자입력)을 통해서 값을 받게되면 항상 문자열 형태로 저장됨!!꼭 기억!!

# #**8-2 다양한 출력 포맷
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500)) # 500 나옴
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))  # +500 나옴
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리 마다 콤마를 찍어주기, +-부호도 붙이기 
# print("{0:+,}".format(100000000000))
# # 3자리 마다 콤마를 찍어주기, +-부호도 붙이기, 30자리수, 빈자리는 ^, 왼쪽정렬
# print("{0:^<+30,}".format(100000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시_소수점 3째 자리에서 반올림하는 예시
# print("{0:.2f}".format(5/3))

# #**8-3 파일 입출력(파이썬을 통해 파일을 불러올 수 있고, 안에 있는 내용을 쓸 수도 있음)
# # 파일 열어서 쓰기 
# score_file = open("score.txt", "w", encoding="utf8") # open(파일명, 용도(w-쓰기), encoding 써주는게 좋음)
# print("수학 : 0", file=score_file) 
# print("영어 : 50", file=score_file)
# score_file.close() # 파일은 항상 열어주면 닫아줘야 함! 
# score_file = open("score.txt", "a", encoding="utf8") # "W"로 하면 덮어쓰기가 되버림! 그래서 "a"(append의미)를 써서 내용 더해주기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # print는 저절로 줄바꿈이 되지만, 파일에서 write 함수는 줄바꿈이 안되기 때문에 '\n'을 사용!
# score_file.close() 
# # 파일 읽어오기_전체 
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) # print를 써야 읽는 내용이 출력되어 볼 수 있음
# score_file.close()
# # 파일 읽어오기_한 줄씩 읽기, 한 줄 읽고 커서는 다음 줄로 이동->한줄씩 띄어져서 출력되는데 바로 밑으로 오게 하고 싶으면 print 구문에서 ','하고 'end=""' 쓰면 됨)
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()
# # 파일이 몇 줄인지 모를 경우(다른사람의 파일인 경우 몇줄인지 모르기 때문)
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="") #한줄 바로 뒤에 오려고 'end=""'입력
# score_file.close()
# # list 형태로 저장
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # 'readlines' 모든 라인을 갖고와서 list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# #**8-4 pickle (프로그램상에서 사용하고 있는 데이터를 파일형태로 저장을 해주는 유용한 라이브러리***)
# #피클_쓰기(우리가 가지고 있는 데이터를 피클을 이용하여 파일에 저장) 
# import pickle
# profile_file = open("profile.pickle", "wb") #pickle은 encoding 할 필요 없음, "wb" w는 쓰기, b는 바이널을 의미 피클을 쓰기 위해서는 항상 바이널타입을 정의를 해줘야 함!
# profile = {"이름":"박명수", "나이":30, "취미": ["축구", "골프", "코딩"]}
# print(profile) # 생략해도 무관 
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file 에 저장
# profile_file.close()
# #피클_불러와서 데이터 읽기(파일에 있는 내용을 load를 통해 불러와서 변수에 저장을 해서 계속 쓸 수 있도록 하는)
# profile_file = open("profile.pickle", "rb") 
# profile = pickle.load(profile_file) # load함수로 file에 있는 정보를 profile에 불러오기 
# print(profile)
# profile_file.close()

# #**8-5 with (이전보다 좀더 수월하게 파일을 읽고 쓸 수 있음-매번 close할 필요 없음)
# import pickle
# with open("profile.pickle", "rb") as profile_file: # 파일을 열어서 profile_file 변수로 저장을 하고,
#     print(pickle.load(profile_file)) # (변수에 저장된) 파일의 내용을 load를 통해서 불러와서 출력을 해주는 것
# # pickle 사용하지 않고 일반적인 파일을 쓰는 경우 
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
# # pickle 사용하지 않고 일반적인 파일을 읽는 경우
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# # 퀴즈7
# #--내가 푼 것--
# for week in range(1,51):
#     with open("{0}주차.txt".format(week), "w", encoding="utf8") as report_file:
#         report_file.write("-{0} 주차 주간보고-\n부서 : \n이름 : \n업무 요약 : ".format(week))
# #--나도코딩--
# for i in range(1,51):
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("-{0} 주차 주간보고-".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")