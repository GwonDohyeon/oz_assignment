#banking_system/models/user.py
from .account import Account
class User:
    def __init__(self,username:str)->None:
        self.account=Account()
        self.username=username