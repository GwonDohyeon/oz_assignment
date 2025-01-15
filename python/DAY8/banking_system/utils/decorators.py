#banking_system/utils/decorators.py
from .exceptions import NegativeAmountError,InsufficientFundsError
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