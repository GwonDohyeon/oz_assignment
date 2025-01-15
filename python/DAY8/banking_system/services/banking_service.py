#banking_system/services/banking_service.py
from utils import UserNotFoundError,InsufficientFundsError,NegativeAmountError
from models import User,Transaction
class Banking_service:
    def __init__(self)->None:
        self.__users=[]
        return
    def add_user(self,username:str)->None:
        user=User(username)
        self.__users.append(user)
        return
    def find_user(self,username:str)->User:
        for i in self.__users:
            if i.username==username:
                return i
        raise UserNotFoundError(username)
    def user_menu(self,username:str)->None:
        user=self.find_user(username)
        while True:
            try:
                num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:잔고 확인, 4:거래내역 보기, 5:나가기): ")
                if num == '5':
                    print(f"'{username}'님 로그아웃.")
                    break
                elif num == '1':  # 입금
                    amount = input("입금할 금액을 입력해주세요: ")
                    amount = int(amount)
                    user.account.deposit(amount)
                    print(f"{amount}원이 입금되었습니다. 현재 잔고는 {user.account.get_balance()}원입니다.")
                elif num == '2':  # 출금
                    amount = input("출금할 금액을 입력해주세요: ")
                    amount = int(amount)
                    user.account.withdraw(amount)
                    print(f"{amount}원이 출금되었습니다. 현재 잔고는 {user.account.get_balance()}원입니다.")
                elif num == '3':  # 잔고 확인
                    print(f"잔액:{user.account.get_balance()}")
                elif num == '4':  # 거래내역 보기
                    transactions=user.account.get_transactions()
                    for i,transaction in enumerate(transactions,start=1):
                        print(f'{i}.{transaction}')
                else:
                    print("유효하지 않은 메뉴입니다. 1, 2, 3, 4, 5 중 하나를 선택해주세요.")
            except NegativeAmountError as e:
                print(f"오류가 발생했습니다: {e} 다시 시도해주세요.")
            except InsufficientFundsError as e:
                print(f"오류가 발생했습니다: {e} 다시 시도해주세요.")
            except Exception as e:
                print(f"예상치 못한 오류가 발생했습니다: {e} 다시 시도해주세요.")
        return
