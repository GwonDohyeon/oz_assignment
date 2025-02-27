#banking_system/models/account.py
from utils import validate_transaction
from .transaction import Transaction
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
    