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