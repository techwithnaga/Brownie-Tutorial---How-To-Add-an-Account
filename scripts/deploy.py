from brownie import accounts

# def deployDefaultAccount():
#     print(accounts[0])

def deployRinkebeTestAccount():
    account = accounts.load("rinkeby_test_account")
    print(account)


def main():
    deployDefaultAccount()

