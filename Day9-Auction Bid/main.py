print('''
      
.______    __       __  .__   __.  _______                         ___      __    __    ______ .___________. __    ______   .__   __. 
|   _  \  |  |     |  | |  \ |  | |       \                       /   \    |  |  |  |  /      ||           ||  |  /  __  \  |  \ |  | 
|  |_)  | |  |     |  | |   \|  | |  .--.  |                     /  ^  \   |  |  |  | |  ,----'`---|  |----`|  | |  |  |  | |   \|  | 
|   _  <  |  |     |  | |  . `  | |  |  |  |                    /  /_\  \  |  |  |  | |  |         |  |     |  | |  |  |  | |  . `  | 
|  |_)  | |  `----.|  | |  |\   | |  '--'  |                   /  _____  \ |  `--'  | |  `----.    |  |     |  | |  `--'  | |  |\   | 
|______/  |_______||__| |__| \__| |_______/                   /__/     \__\ \______/   \______|    |__|     |__|  \______/  |__| \__| 
                                                                                                                                                                                                                                                                      
 ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______  ______        
|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______||______|
                                                                                                                                                                                                                                                         
      ''')


def finding_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"Congratulation! The highest bidder is {winner} with a ${highest_bid} bid.")


bids = {}
continued_bids = True
while continued_bids:
    name = input("Enter your name: ")
    price = float(input("Enter the price you want to bid : $"))
    bids[name] = price
    should_continue = input("Is there any other Bidders, Type 'yes' or 'no'.: ").lower()
    if should_continue == "no":
        finding_highest_bidder(bids)
        continued_bids = False
    elif should_continue == "yes":
        print("\n" * 100)
        continued_bids = True
    else:
        print("Wrong Input!")



