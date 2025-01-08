#while문을 이용해서 입금, 출금, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기 전까지 계속해서 노출되도록 만들어주세요
#종료를 누르면 서비스를 종료한다는 메시지를 출력하고 현재 잔액을 보여주세요
#입력 검증 및 에러 처리 추가
#잘못된 입력 값(숫자가 아닌값, 음수 값 등)을 처리하도록 기능을 추가해주세요
#유효하지 않은 메뉴 선택 시 경고 메시지 또는 사용방법 재안내를 해주세요
balance=3000
receipts=[]
while True:
    num=input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)")
    if num=='4':
        break
    if num=='1':
        deposit_amount=int(input("입금할 금액을 입력해주세요:"))
        balance+=deposit_amount
        receipts.append(("입금",deposit_amount,balance))
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')
    if num=='2':
        withdraw_amount=int(input("출금할 금액을 입력해주세요:"))
        withdraw_amount=min(balance,withdraw_amount)
        balance-=withdraw_amount
        receipts.append(("출금",withdraw_amount,balance))
        print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.')
        
print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.')