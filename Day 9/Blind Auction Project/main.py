import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into bidding_dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in bidding_dictionary


person_data = []
bidding_data = []

def bidding_function():
    person = input('Enter your name: \n')
    price = int(input('Enter your bidding price: \n$'))
    person_data.append(person)
    bidding_data.append(price)
    print("\n" * 100)
    other_bidders = input("Are there any other any bidder? Type 'yes' to input data else Type 'no': \n")
    if other_bidders == 'yes':
        bidding_function()
    elif other_bidders == 'no':
        #sample_dictionary[person] = price
        sample_dictionary = dict(zip(person_data, bidding_data))
        max_bid = max(sample_dictionary, key=sample_dictionary.get)
        print(f"The Winner is {max_bid} with the amount ${sample_dictionary[max_bid]}")
    else:
        print('Invalid input, restart program')


bidding_function()
