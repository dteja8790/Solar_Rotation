from ATMExcept import DepositError,WithDrawError,InsufficientFundError
balance=500.00
def deposit():
    depositAmt=float(input("Enter UR Deposit Amount:"))
    if(depositAmt<=0):
        raise DepositError
    else:
        global balance
        balance=balance+depositAmt
        print("\tUr Account xxxxxx6350 Credited with INR:{}".format(depositAmt))
        print("\tUr Account xxxxxx6350 Bal after desposit:{}".format(balance))

def withdraw():
    global balance
    withdrawAmt = float(input("Enter UR Withdraw Amount:"))
    if(withdrawAmt<=0):
        raise WithDrawError
    elif((withdrawAmt+500)>balance):
        raise InsufficientFundError
    else:
        balance=balance-withdrawAmt
        print("\tUr Account xxxxxx6350 Debited with INR:{}".format(withdrawAmt))
        print("\tUr Account xxxxxx6350 Bal after Withdraw:{}".format(balance))

def balenq():
    print("\tUr Account xxxxxx6350 Balance:{}".format(balance))