pragma solidity >=0.4.25 <0.6.0;


contract AlmostSmartAuction {
  enum AuctionStates { BidState, FinishedState}
  AuctionStates myState;

  mapping (address => uint) bids;
  uint blocklimit;
  address winner;
  uint winnerBid;

  constructor(uint auctionTime) public {
    blocklimit= block.number + auctionTime;
    myState = AuctionStates.BidState;
    winnerBid = 0;
  }

  function bid(uint bidValue) public {
    verifyFinished();
    require ( myState ==  AuctionStates.BidState, "Bids closed...");
    if (bidValue > winnerBid) {
      winnerBid = bidValue;
      winner = msg.sender;
      }
  }


  function verifyFinished() private {
    if (block.number > blocklimit) {
      myState = AuctionStates.FinishedState;
      }
    }

  function isWinner(address who) public returns (bool) {
    verifyFinished();
    require ( myState ==  AuctionStates.FinishedState, "Be patient...");
    return who==winner;
  }
}
