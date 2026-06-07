from ATMExcept import DepositError,WithDrawError,InsufficientFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
while(True):
    try:
        menu()
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                balenq()
            case 2:
                try:
                    deposit()
                except DepositError:
                    print("\tDON'T TRY TO DEPOSIT NEGATIVE/ZERO VALUE")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR DEPOSIT AMOUNT")
            case 3:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDON'T TRY TO WITHDRAW NEGATIVE/ZERO VALUE")
                except InsufficientFundError:
                    print("\tYOUR ACCOUNT DOES NOT CONTAIN STUFF FUNDS")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR WITHDRAW AMOUNT")
            case 4:
                print("THANKS FOR USING........")
                break
            case _:
                print("\tYOUR SELECTION OF CHOICE IS WRONG TRY-AGAIN")
    except ValueError:
        print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR WITHDRAW AMOUNT")
