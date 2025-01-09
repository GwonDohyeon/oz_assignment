balance = 3000
receipts = []

while True:
    try:
        # 메뉴 선택 입력
        num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료): ")
        
        if num == '4':
            print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.')
            break

        elif num == '1':  # 입금
            deposit_amount = input("입금할 금액을 입력해주세요: ")
            if not deposit_amount.isdigit() or int(deposit_amount) <= 0:
                print("유효하지 않은 금액입니다. 양수 숫자를 입력해주세요.")
                continue
            deposit_amount = int(deposit_amount)
            balance += deposit_amount
            receipts.append(("입금", deposit_amount, balance))
            print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')

        elif num == '2':  # 출금
            withdraw_amount = input("출금할 금액을 입력해주세요: ")
            if not withdraw_amount.isdigit() or int(withdraw_amount) <= 0:
                print("유효하지 않은 금액입니다. 양수 숫자를 입력해주세요.")
                continue
            withdraw_amount = int(withdraw_amount)
            if withdraw_amount > balance:
                print(f"잔액이 부족합니다. 현재 잔액은 {balance}원 입니다.")
                continue
            balance -= withdraw_amount
            receipts.append(("출금", withdraw_amount, balance))
            print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.')

        elif num == '3':  # 영수증 보기
            if not receipts:
                print("영수증 내역이 없습니다.")
            else:
                print("\n--- 영수증 내역 ---")
                for idx, (action, amount, current_balance) in enumerate(receipts, start=1):
                    print(f'{idx}. {action}: {amount}원, 잔액: {current_balance}원')
                print("-------------------\n")

        else:
            print("유효하지 않은 메뉴입니다. 1, 2, 3, 4 중 하나를 선택해주세요.")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}. 다시 시도해주세요.")
