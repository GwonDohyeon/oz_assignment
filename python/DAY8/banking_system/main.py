#banking_system/main.py
from services import Banking_service
from utils import UserNotFoundError
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
if __name__=="__main__":
    main()