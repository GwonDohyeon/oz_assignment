#banking_system/utils/decorators.py
"""class validate_transaction:
    def __init__(self,func):
        self.func=func
    def __call__(self,amount,*args,**kwargs):
        if amount <=0:
            raise ValueError("금액은 0보다 큰 값을 입력하세요.")
        result=self.func(amount,*args,**kwargs)
        return result 
"""
def validate_transaction(func:callable)->callable:
    def wrapper(amount,*args,**kwargs):
        if amount <=0:
            raise ValueError("금액은 0보다 큰 값을 입력하세요.")
        result=func(amount,*args,**kwargs)
        return result
    return wrapper