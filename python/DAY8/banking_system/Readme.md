### 온라인 뱅킹 시스템 만들어보기

온라인 뱅킹 시스템"을 만드는 것입니다. 

이 시스템은 사용자가 자신의 계좌를 관리하고 거래를 기록하며, 입금, 출금, 잔고 확인 및 거래 내역을 확인할 수 있는 기능을 제공합니다. 

각 기능은 개별적인 클래스로 구현되며, 타입 힌팅과 예외 처리를 통해 견고한 코드를 작성하는 연습을 할 수 있습니다.

-----

### 프로젝트 구성 요소
#### 1. Transaction 클래스:

거래 내역을 나타내는 클래스입니다. 거래 유형, 금액, 잔고를 속성으로 가지고 있습니다.
문자열로 거래 내역을 반환하는 메서드와 튜플로 반환하는 메서드를 구현합니다.

#### 2. Account 클래스:

계좌를 나타내는 클래스입니다. 잔고와 거래 내역을 관리합니다.
입금, 출금, 잔고 확인 및 거래 내역을 반환하는 메서드를 구현합니다.
클래스 변수로 은행 이름을 관리하고, 이를 설정하고 반환하는 메서드를 구현합니다.

#### 3. User 클래스:

사용자를 나타내는 클래스입니다. 사용자 이름과 계좌를 속성으로 가지고 있습니다.
생성자를 통해 사용자 이름과 계좌를 초기화합니다.

#### 4. BankingService 클래스:
여러 사용자를 관리하는 서비스 클래스입니다.
사용자를 추가하고, 찾고, 사용자 메뉴를 제공하는 메서드를 구현합니다.

#### 5. 데코레이터 및 예외 처리:
거래 금액이 유효한지 확인하는 데코레이터를 구현합니다.
잔고 부족, 음수 금액 입력, 사용자 찾기 실패 등의 상황을 처리하는 사용자 정의 예외 클래스를 구현합니다.

#### 6. 메인 함수:

사용자로부터 입력을 받아 사용자를 추가하거나 찾고, 사용자 메뉴를 통해 입금, 출금, 잔고 확인, 거래 내역 기능을 제공하는 메인 함수를 구현합니다.

-----

### 각 클래스와 메서드의 상세 설명
#### Transaction 클래스:

__init__(self, transaction_type: str, amount: int, balance: int) -> None: 거래 유형, 금액, 잔고를 초기화합니다.
__str__(self) -> str: 거래 정보를 문자열로 반환합니다.
to_tuple(self) -> tuple: 거래 정보를 튜플로 반환합니다.

#### Account 클래스:

__init__(self) -> None: 잔고와 거래 내역을 초기화합니다.
deposit(self, amount: int) -> None: 금액을 입금하고, 거래 내역에 추가합니다.
withdraw(self, amount: int) -> None: 금액을 출금하고, 거래 내역에 추가합니다.
get_balance(self) -> int: 현재 잔고를 반환합니다.
get_transactions(self) -> list: 거래 내역을 반환합니다.
get_bank_name(cls) -> str: 은행 이름을 반환하는 클래스 메서드입니다.
set_bank_name(cls, name: str) -> None: 은행 이름을 설정하는 클래스 메서드입니다.

#### User 클래스:

__init__(self, username: str) -> None: 사용자 이름과 계좌를 초기화합니다.
BankingService 클래스:

__init__(self) -> None: 사용자 목록을 초기화합니다.
add_user(self, username: str) -> None: 사용자를 추가합니다.
find_user(self, username: str) -> User: 사용자를 찾습니다.
user_menu(self, username: str) -> None: 사용자 메뉴를 제공합니다.

#### 데코레이터 및 예외 처리:

validate_transaction(func: Callable) -> Callable: 거래 금액이 유효한지 확인하는 데코레이터입니다.
InsufficientFundsError(Exception): 잔고 부족 상황을 처리하는 예외 클래스입니다.
NegativeAmountError(Exception): 음수 금액 입력 상황을 처리하는 예외 클래스입니다.
UserNotFoundError(Exception): 사용자 찾기 실패 상황을 처리하는 예외 클래스입니다.

#### 메인 함수:

main() -> None: BankingService 인스턴스를 생성하고, 사용자로부터 입력을 받아 사용자 추가 및 찾기 기능을 제공하며, 사용자 메뉴를 통해 입금, 출금, 잔고 확인, 거래 내역 기능을 실행합니다.

### 프로젝트의 목표
이 프로젝트의 목표는 다음과 같습니다:

1. 객체 지향 프로그래밍: 클래스를 정의하고, 객체를 생성하며, 객체 간의 상호작용을 구현합니다.
2. 타입 힌팅: 타입 힌팅을 사용하여 코드의 가독성과 안정성을 높입니다.
3. 예외 처리: 다양한 예외 상황을 처리하여 견고한 코드를 작성합니다.
4. 사용자 입력 처리: 사용자로부터 입력을 받아 시스템을 작동시키는 인터페이스를 구현합니다.

### 기대 효과
이 프로젝트를 통해 다음과 같은 효과를 기대할 수 있습니다:

- 클래스와 객체: 클래스를 정의하고 객체를 생성하며, 객체 간의 상호작용을 이해할 수 있습니다.
- 타입 힌팅: 타입 힌팅을 사용하여 함수와 메서드의 인자와 반환 타입을 명확히 정의할 수 있습니다.
- 예외 처리: 다양한 예외 상황을 처리하여 프로그램의 안정성을 높일 수 있습니다.
- 사용자 입력 처리: 사용자 입력을 처리하고, 입력에 따라 프로그램이 적절히 동작하도록 구현할 수 있습니다.

이 프로젝트는 다양한 프로그래밍 개념을 종합적으로 활용하여 실습할 수 있는 좋은 기회가 될 것입니다.<br>
각 과제를 해결하면서 객체 지향 프로그래밍, 타입 힌팅, 예외 처리 등의 개념을 깊이 이해하고 응용할 수 있습니다.

----- 

#### 과제 1: Transaction 클래스 구현
파일명: banking_system/models/transaction.py

<b>해결해야 할 과제 및 요구 사항:</b>

1. 거래(Transaction) 클래스를 정의하고, transaction_type, amount, balance 속성을 초기화하는 생성자를 구현합니다.
2. 거래 정보를 문자열로 반환하는 __str__ 메서드를 구현합니다.
3. 거래 정보를 튜플로 반환하는 to_tuple 메서드를 구현합니다.

<b>변수 컨벤션:</b>

- transaction_type: 거래 유형을 나타내는 문자열 (예: "입금", "출금")
- amount: 거래 금액을 나타내는 정수
- balance: 거래 후 잔고를 나타내는 정수

##### 문제 1.1: 생성자 구현

- transaction_type, amount, balance 속성을 초기화하는 생성자를 구현하세요.
- 타입 힌팅을 사용하여 생성자의 매개변수 타입을 지정하세요.
    - 함수 시그니처: __init__(self, transaction_type: str, amount: int, balance: int) -> None
'''python
#banking_system/models/transaction.py
class Transaction:
    def __init__(self,transaction_type:str,amount:int,balance:int)->None:
        self.transaction_type=transaction_type
        self.amount=amount
        self.balance=balance
'''
##### 문제 1.2: 문자열 반환 메서드 구현

- 거래 정보를 문자열로 반환하는 __str__ 메서드를 구현하세요.
- 타입 힌팅을 사용하여 메서드의 반환 타입을 지정하세요.
    - 함수 시그니처: __str__(self) -> str
'''python
#banking_system/models/transaction.py
class Transaction:
    def __init__(self,transaction_type:str,amount:int,balance:int)->None:
        self.transaction_type=transaction_type
        self.amount=amount
        self.balance=balance
    
    def __str__(self)->str:
        return f"거래내역:{self.transaction_type}, 입출금액:{self.amount}, 잔액:{self.balance}"
'''
##### 문제 1.3: 튜플 반환 메서드 구현

- 거래 정보를 튜플로 반환하는 to_tuple 메서드를 구현하세요.
- 타입 힌팅을 사용하여 메서드의 반환 타입을 지정하세요.
    - 함수 시그니처: to_tuple(self) -> tuple
'''python
#banking_system/models/transaction.py
class Transaction:
    def __init__(self,transaction_type:str,amount:int,balance:int)->None:
        self.transaction_type=transaction_type
        self.amount=amount
        self.balance=balance
    
    def __str__(self)->str:
        return f"거래내역:{self.transaction_type}, 입출금액:{self.amount}, 잔액:{self.balance}"
    
    def to_tuple(self)->tuple:
        return tuple(self.transaction_type,self.amount,self.balance)
'''
#### 과제 2: Account 클래스 구현
파일명: banking_system/models/account.py

<b>해결해야 할 과제 및 요구 사항:</b>

1. __balance와 transactions 리스트를 초기화하는 생성자를 구현합니다.
2. 입금을 위한 deposit 메서드를 구현합니다.
3. 출금을 위한 withdraw 메서드를 구현합니다.
4. 잔고를 반환하는 get_balance 메서드를 구현합니다.
5. 거래 내역을 반환하는 get_transactions 메서드를 구현합니다.
6. 클래스 변수 bank_name와 클래스 메소드 get_bank_name, set_bank_name을 구현합니다.

<b>변수 컨벤션:</b>

- __balance: 계좌 잔고를 나타내는 프라이빗 정수 변수
- transactions: 거래 내역을 저장하는 리스트
- bank_name: 은행 이름을 나타내는 클래스 변수 문자열
- amount: 입금 또는 출금 금액을 나타내는 정수

##### 문제 2.1: 생성자 구현

- __balance와 transactions 리스트를 초기화하는 생성자를 구현하세요.
- 타입 힌팅을 사용하여 생성자의 매개변수 타입을 지정하세요.
    - 함수 시그니처: __init__(self) -> None
'''python
#banking_system/models/account.py
class Account:
    def __init__(self)->None:
        self.transactions=[]
        self.__balance=0
'''
##### 문제 2.2: 입금 메서드 구현

- 입금을 위한 deposit 메서드를 구현하세요.
- 금액이 양수인지 확인한 후 잔고를 증가시키고, 거래 내역에 추가합니다.
- 타입 힌팅을 사용하여 메서드의 매개변수와 반환 타입을 지정하세요.
    - 함수 시그니처: deposit(self, amount: int) -> None
'''python
#banking_system/models/account.py
class Account:
    def __init__(self)->None:
        self.transactions=[]
        self.__balance=0
    def deposit(self,amount:int)->None:
        if amount>0:
            self.__balance+=amount
            self.transactions.append(Transaction("입금",amount,self.__balance))
'''       
##### 문제 2.3: 출금 메서드 구현

- 출금을 위한 withdraw 메서드를 구현하세요.
- 금액이 잔고보다 크지 않고 양수인지 확인한 후 잔고를 감소시키고, 거래 내역에 추가합니다.
- 타입 힌팅을 사용하여 메서드의 매개변수와 반환 타입을 지정하세요.
    - 함수 시그니처: withdraw(self, amount: int) -> None
'''python
#banking_system/models/account.py
class Account:
    def __init__(self)->None:
        self.transactions=[]
        self.__balance=0
    def deposit(self,amount:int)->None:
        if amount>0:
            self.__balance+=amount
            self.transactions.append(Transaction("입금",amount,self.__balance))
        return
    def withdraw(self,amount:int)->None:
        if amount>0 and not amount>self.__balance:
            self.__balance-=amount
            self.transactions.append(Transaction("출금",amount,self.__balance))
        return
'''            
##### 문제 2.4: 잔고 반환 메서드 구현

- 잔고를 반환하는 get_balance 메서드를 구현하세요.
- 타입 힌팅을 사용하여 메서드의 반환 타입을 지정하세요.
    - 함수 시그니처: get_balance(self) -> int
'''python
#banking_system/models/account.py
class Account:
    def __init__(self)->None:
        self.transactions=[]
        self.__balance=0
    def deposit(self,amount:int)->None:
        if amount>0:
            self.__balance+=amount
            self.transactions.append(Transaction("입금",amount,self.__balance))
        return
    def withdraw(self,amount:int)->None:
        if amount>0 and not amount>self.__balance:
            self.__balance-=amount
            self.transactions.append(Transaction("출금",amount,self.__balance))
        return
    def get_balance(self)->int:
        return self.__balance
'''
##### 문제 2.5: 거래 내역 반환 메서드 구현

- 거래 내역을 반환하는 get_transactions 메서드를 구현하세요.
- 타입 힌팅을 사용하여 메서드의 반환 타입을 지정하세요.
    - 함수 시그니처: get_transactions(self) -> list
'''python
#banking_system/models/account.py
class Account:
    def __init__(self)->None:
        self.transactions=[]
        self.__balance=0
    def deposit(self,amount:int)->None:
        if amount>0:
            self.__balance+=amount
            self.transactions.append(Transaction("입금",amount,self.__balance))
        return
    def withdraw(self,amount:int)->None:
        if amount>0 and not amount>self.__balance:
            self.__balance-=amount
            self.transactions.append(Transaction("출금",amount,self.__balance))
        return
    def get_balance(self)->int:
        return self.__balance
    def get_transactions(self)->list:
        return self.transactions
'''
##### 문제 2.6: 클래스 변수 및 메서드 구현

- 클래스 변수 bank_name와 클래스 메소드 get_bank_name, set_bank_name을 구현하세요.
- 타입 힌팅을 사용하여 클래스 메서드의 매개변수와 반환 타입을 지정하세요.
    - 함수 시그니처:
        - get_bank_name(cls) -> str
        - set_bank_name(cls, name: str) -> None
'''python
#banking_system/models/account.py
class Account:
    bank_name="oz_bank"
    def __init__(self)->None:
        self.transactions=[]
        self.__balance=0
    @validate_transaction
    def deposit(self,amount:int)->None:
        self.__balance+=amount
        self.transactions.append(Transaction("입금",amount,self.__balance))
        return
    @validate_transaction
    def withdraw(self,amount:int)->None:
        self.__balance-=amount
        self.transactions.append(Transaction("출금",amount,self.__balance))
        return
    def get_balance(self)->int:
        return self.__balance
    def get_transactions(self)->list:
        return self.transactions
    @classmethod
    def get_bank_name(cls)->str:
        return cls.bank_name
    @classmethod
    def set_bank_name(cls,name:str)->None:
        cls.bank_name=name
        return
'''   
#### 과제 3: User 클래스 구현
파일명: banking_system/models/user.py

<b>해결해야 할 과제 및 요구 사항:</b>

username과 account를 초기화하는 생성자를 구현합니다.

<b>변수 컨벤션:</b>

username: 사용자의 이름을 나타내는 문자열
account: 사용자의 계좌를 나타내는 Account 객체

##### 문제 3.1: 생성자 구현

- username과 account를 초기화하는 생성자를 구현하세요.
- 타입 힌팅을 사용하여 생성자의 매개변수 타입을 지정하세요.
    - 함수 시그니처: __init__(self, username: str) -> None
'''python
#banking_system/models/user.py
class User:
    def __init__(self,username:str)->None:
        self.account=Account()
        self.username=username
'''
#### 과제 4: BankingService 클래스 구현
파일명: banking_system/services/banking_service.py

<b>해결해야 할 과제 및 요구 사항:</b>

1. 사용자 목록을 초기화하는 생성자를 구현합니다.
2. 사용자를 추가하는 add_user 메서드를 구현합니다.
3. 사용자를 찾는 find_user 메서드를 구현합니다.
4. 사용자 메뉴를 제공하는 user_menu 메서드를 구현합니다.

<b>변수 컨벤션:</b>

- users: 사용자 목록을 저장하는 리스트
- username: 사용자의 이름을 나타내는 문자열
- user: User 객체를 나타내는 변수
- amount: 입금 또는 출금 금액을 나타내는 정수
- choice: 사용자의 선택을 나타내는 문자열

##### 문제 4.1: 생성자 구현

- 사용자 목록을 초기화하는 생성자를 구현하세요.
- 타입 힌팅을 사용하여 생성자의 매개변수 타입을 지정하세요.
    - 함수 시그니처: __init__(self) -> None
'''python
#banking_system/services/banking_service.py
class Banking_service:
    def __init__(self)->None:
        self.__users:list[User]=[]
        return
'''
##### 문제 4.2: 사용자 추가 메서드 구현

- 사용자를 추가하는 add_user 메서드를 구현하세요.
- User 객체를 생성하여 사용자 목록에 추가합니다.
- 타입 힌팅을 사용하여 메서드의 매개변수와 반환 타입을 지정하세요.
    - 함수 시그니처: add_user(self, username: str) -> None
'''python
#banking_system/services/banking_service.py
class Banking_service:
    def __init__(self)->None:
        self.__users:list[User]=[]
        return
    def add_user(self,username:str)->None:
        user=User(username)
        self.__users.append(user)
        return
'''
##### 문제 4.3: 사용자 찾기 메서드 구현

- 사용자를 찾는 find_user 메서드를 구현하세요.
- 사용자 목록을 검색하여 해당 사용자를 반환하고, 없으면 예외를 발생시킵니다.
- 타입 힌팅을 사용하여 메서드의 매개변수와 반환 타입을 지정하세요.
    - 함수 시그니처: find_user(self, username: str) -> User
'''python
#banking_system/services/banking_service.py
class Banking_service:
    def __init__(self)->None:
        self.__users:list[User]=[]
        return
    def add_user(self,username:str)->None:
        user=User(username)
        self.__users.append(user)
        return
    def find_user(self,username:str)->User:
        for i in self.__users:
            if i.username==username:
                return i
        raise Exception(f"{username}이(가) 존재하지 않습니다.")
'''
##### 문제 4.4: 사용자 메뉴 제공 메서드 구현

- 사용자 메뉴를 제공하는 user_menu 메서드를 구현하세요.
- 사용자를 찾고, 입금, 출금, 잔고 확인, 거래 내역 기능을 제공하는 반복 루프를 구현합니다.
- 타입 힌팅을 사용하여 메서드의 매개변수와 반환 타입을 지정하세요.
    - 함수 시그니처: user_menu(self, username: str) -> None
'''python
#banking_system/services/banking_service.py
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
                    amount=int(amount)
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
                print(f"오류가 발생했습니다: {e} 다시 시도해주세요.")
        return
'''
#### 과제 5: 데코레이터 및 예외 처리 구현
파일명: banking_system/utils/decorators.py, banking_system/utils/exceptions.py

<b>해결해야 할 과제 및 요구 사항:</b>

1. validate_transaction 데코레이터를 작성하여 금액이 0보다 큰지 확인합니다.
2. 사용자 정의 예외 클래스 InsufficientFundsError, NegativeAmountError, UserNotFoundError를 작성합니다.

##### 문제 5.1: 데코레이터 구현

- validate_transaction 데코레이터를 작성하여 금액이 0보다 큰지 확인합니다.
- 타입 힌팅을 사용하여 함수의 매개변수와 반환 타입을 지정하세요.
    - 함수 시그니처: validate_transaction(func: Callable) -> Callable
'''python
#banking_system/utils/decorators.py
"""class validate_transaction:
    def __init__(self,func):
        self.func=func
    def __call__(self,amount,*args,**kwargs):
        if amount <0:
            raise NegativeAmountError()
        if func.__name__=="withdraw" and amount > self.get_balance():
            raise InsufficientFundsError(self.get_balance())
        result=func(self,amount,*args,**kwargs)
        return result
"""
def validate_transaction(func:callable)->callable:
    def wrapper(self,amount:int,*args,**kwargs):
        if amount <0:
            raise NegativeAmountError()
        if func.__name__=="withdraw" and amount > self.get_balance():
            raise InsufficientFundsError(self.get_balance())
        result=func(self,amount,*args,**kwargs)
        return result
    return wrapper
'''
#### 문제 5.2: 사용자 정의 예외 클래스 구현

- 사용자 정의 예외 클래스 InsufficientFundsError, NegativeAmountError, UserNotFoundError를 작성하세요.
- 각 예외 클래스에 타입 힌팅을 사용하여 생성자의 매개변수와 반환 타입을 지정하세요.
    - 함수 시그니처:
        - InsufficientFundsError.__init__(self, balance: int) -> None
        - NegativeAmountError.__init__(self) -> None
        - UserNotFoundError.__init__(self, username: str) -> None
'''python
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
'''
#### 과제 6: 메인 함수 구현
파일명: banking_system/main.py

<b>해결해야 할 과제 및 요구 사항:</b>

1. BankingService 인스턴스를 생성합니다.
2. 사용자로부터 입력을 받아 사용자 추가 및 찾기 기능을 제공합니다.
3. 사용자 메뉴를 통해 입금, 출금, 잔고 확인, 거래 내역 기능을 실행할 수 있도록 합니다.

##### 문제 6.1: 메인 함수 구현

- BankingService 인스턴스를 생성하세요.
- 사용자로부터 입력을 받아 사용자 추가 및 찾기 기능을 구현하세요.
- 사용자 메뉴를 통해 입금, 출금, 잔고 확인, 거래 내역 기능을 실행할 수 있도록 구현하세요.
- 타입 힌팅을 사용하여 함수의 매개변수와 반환 타입을 지정하세요.
    - 함수 시그니처: main() -> None
'''python
#banking_system/main.py
def main()->None:
    banking_service=Banking_service()
    while True:
        try:
            username=input("계정주의 이름을 입력하세요:")
            user=banking_service.find_user(username)
            banking_service.user_menu(user.username)
            q=input("시스템을 종료하시겠습니까? (Y/N):")
            if(q=="Y"):
                break    
        except UserNotFoundError as e:
            print(e)
            add=input(f"{username}의 계정을 새로 만드시겠습니까? (Y/N):")
            if(add=='Y'):
                banking_service.add_user(username)
                user=banking_service.find_user(username)
                banking_service.user_menu(user.username)
            q=input("시스템을 종료하시겠습니까? (Y/N):")
            if(q=="Y"):
                break             
        except Exception as e:
            print(e)
    return
'''