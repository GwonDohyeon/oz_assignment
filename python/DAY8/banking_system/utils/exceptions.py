#banking_system/utils/exceptions.py
class InsufficientFundsError(Exception):
    def __init__(self,balance:int)->None:
        self.balance=balance
        super().__init__(f"잔액이 부족합니다, 현재 잔액:{self.balance}")
class NegativeAmountError(Exception):
    def __init__(self)->None:
        super().__init__(f"금액은 음수일 수 없습니다.")
class UserNotFoundError(Exception):
    def __init__(self,username:str)->None:
        self.username = username
        super().__init__(f"사용자 '{username}'를 찾을 수 없습니다.")