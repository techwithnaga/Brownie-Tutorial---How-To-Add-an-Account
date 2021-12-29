from brownie import accounts


def deploy():
    account = accounts.load("rinkeby_test_account")
    print(account)


def main():
    deploy()
