# importing clear function
from replit import clear

# To display logo
from art import logo
print(logo)

# State variables 
bids = {}
bidding_finished = False

# Bidding Process. Each bidder and their bid amount is stored. Continues until bidding is bidding_finished
while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    highest_bidder(bids)
  elif should_continue == "yes":
    
    

    def highest_bidder(bidding_record):
      highest_bid = 0
      winner = ""
      
      # bidding_record = name, bid amount
      for bidder in bidding_record:
          
      # Check for highest bidder      
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
          highest_bid = bid_amount
          winner = bidder
      
      print(f"The winner is {winner} with a bid of ${highest_bid}")