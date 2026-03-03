auction={}

want_to_continue=True
while want_to_continue:
    name=input("what is your name ")
    bid=int(input("what is your bid "))
    auction[name]=bid
    continuation=input("anyone else want to place their bid")
    print("\n"*100)
    if continuation == "n":
        want_to_continue=False
print(auction)
highest_bid=0
highest_bidder=""
for key in auction:
    if auction[key] >=highest_bid:
        highest_bid=auction[key]
        highest_bidder=key
print(f"the highest bid is {highest_bid}, and the winner is {highest_bidder}")


