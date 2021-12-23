from brownie import *
import brownie

def main():
    auction = AlmostSmartAuction.deploy(4,{'from': accounts[0]})

    auction.bid(10,{'from': accounts[1]})
    auction.bid(12,{'from': accounts[2]})
    auction.bid(13,{'from': accounts[1]})
    auction.bid(14,{'from': accounts[3]})
    try:
        auction.bid(16,{'from': accounts[4]})
    except:
        print('Fail...')


    print(auction.isWinner.call(accounts[1].address,{'from': accounts[1]}))
    print(auction.isWinner.call(accounts[2].address,{'from': accounts[0]}))
    print(auction.isWinner.call(accounts[3].address,{'from': accounts[5]}))
