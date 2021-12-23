from brownie import *
import brownie

def main():
    token = VerySimpleToken.deploy("Token1",{'from': accounts[0]})

    token.transfer(accounts[1],{'from':accounts[0]})

    try:
        token.transfer(accounts[2],{'from':accouts[0]})
    except:
        print('Fail...')


    print(token.isOwner.call(accounts[1].address,{'from': accounts[1]}))
