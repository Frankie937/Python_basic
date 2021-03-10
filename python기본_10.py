# #**10-1 예외처리 (어떤 에러가 발생했을 때 그에 대해서 처리를 해주는 것)
# try: 
# # 나누기전용 계산기 프로그램 
#     print("나누기 전용 계산기입니다.")
#     nums =[] 
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError: #숫자가 아닌 '삼' 이런식으로 넣을 경우
#     print("에러! 잘못된 값을 입력하였습니다.") 
# except ZeroDivisionError as err: # 나누는 값을 0을 넣을 경우(나누기에서 0으로 나눌 수 없음)
#     print(err)
# except Exception as err: # 위에 2개 에러 말고 다른 에러들 발생할 경우 ('err'은 무슨 에러인지 알려주는 것)
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# #**10-2 에러 발생시키기(의도적으로 에러를 발생시키는 것)
# #한 자리 숫자 나누기 전용 계산기
# try: 
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError # 에러를 내가 원하는 조건에 해당하는 경우, 'raise'를 사용하여 의도적으로 만들 수 있음 
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/ num2)))
# except ValueError: 
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# #**10-3 사용자 정의 예외처리(파이썬에서 정의하는 에러(ValueError, ZeroDivisionError 등)가 아닌 사용자가 직접 만든 에러를 처리하는 것)
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg
# try: 
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 사용자가 클래스를 사용하여 만든 에러 
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/ num2)))
# except ValueError: 
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해주셔서 감사합니다.")
# #**10-4 finally(예외처리 구문에서 정상적으로 수행이 되건 오류가 발생하건 상관없이 무조건 실행되는 구문)
# #항상 try 구문 내에서 맨 마지막에 작성

# #**퀴즈 9
# #--내가 푼 것
# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작 
# while(True):
#     try: 
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:  # 남은 치킨보다 주문량이 많을 때 
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
#             if chicken <= 0 :
#                 raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#     except ValueError: 
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as err:
#         print(err)
#         break # while문 탈출(프로그램 종료)

# # --나도코딩--
# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작 
# while(True):
#     try: 
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:  # 남은 치킨보다 주문량이 많을 때 
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken <= 0 :
#             raise SoldOutError
#     except ValueError: 
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as err:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break # while문 탈출(프로그램 종료)