from brownie import *
import brownie

def main():

    contractOwner = accounts[0]
    tokenOwner = accounts[1]

    bidder1 = accounts[2]
    bidder2 = accounts[3]
    bidder3 = accounts[4]
    bidderFake = accounts[5]

    token = VerySimpleToken.deploy("Token1",{'from': tokenOwner})
    auction = TokenAuction.deploy(100,50,{'from': contractOwner})

    auction.createAuction("Leilao1", 12, token,{'from':tokenOwner})

    token.transfer(auction,{'from':tokenOwner})

    auction.initAuction("Leilao1")

    auction.sendCollateral("Leilao1",{'from':bidder1,'value':100})
    auction.sendCollateral("Leilao1",{'from':bidder2,'value':100})
    auction.sendCollateral("Leilao1",{'from':bidder3,'value':100})


    auction.bid("Leilao1",1000,{'from':bidder1})
    auction.bid("Leilao1",1010,{'from':bidder2})
    auction.bid("Leilao1",1020,{'from':bidder3})
    auction.bid("Leilao1",1010,{'from':bidder1})
    auction.bid("Leilao1",1050,{'from':bidder2})

    try:
        auction.bid("Leilao1",1099,{'from':bidderFake})
    except:
        print("Dont!!")


    try:
        auction.bid("Leilao1",1000,{'from':bidder1})
        auction.bid("Leilao1",1000,{'from':bidder1})
        auction.bid("Leilao1",1000,{'from':bidder1})
        auction.bid("Leilao1",1000,{'from':bidder1})
        auction.bid("Leilao1",1000,{'from':bidder1})
    except:
        print("Dont!!")

    auction.claimToken("Leilao1",{'from':bidder2,'value':1050-100})


    auction.claimCollateral("Leilao1",{'from':bidder1})
    try:
        auction.claimCollateral("Leilao1",{'from':bidder2})
    except:
        print('Tentei roubar...mas nao consegui...')

    auction.claimCollateral("Leilao1",{'from':bidder3})
    auction.getProfit("Leilao1",{'from':contractOwner})
    auction.getFee({'from':tokenOwner})

    print(bidder1.balance())
    print(bidder2.balance())
    print(token.isOwner.call(bidder2))
    print(bidder3.balance())
    print(contractOwner.balance())
    print(tokenOwner.balance())
