import random

suits = ['\u2660','\u2661','\u2662','\u2663']
values =['A','2','3','4','5','6','7','8','9','10','J','Q','K']

# getting the sum
def getSum(pack):

    sum = 0
    aCount = 0
    for i in range(0, len(pack)):
        if pack[i][0:-1] == 'A':
            aCount+=1
            sum += 1
        elif pack[i][0:-1] == 'J':
            sum += 11
        elif pack[i][0:-1] == 'Q':
            sum += 12
        elif pack[i][0:-1] == 'K':
            sum += 13
        else:
            sum += int(pack[i][0:-1])
    if aCount > 0:
        if sum + 10 < 21:
            return sum+10
    return sum
    

def card_shuffle_and_dealing(deck,player,house):    
    c = ''
    # creating the deck of cards
    for s in suits:
        for v in values:
            c = v + s
            deck.append(c)
    
    #shuffling the deck of cards
    random.shuffle(deck)
    print(deck)
    print(len(deck))
    print()
    # dealing the cards 
    for i in range(0,4):
        if i%2 == 0:
            player.append(deck[i]) 
        else:
            house.append(deck[i])

    # removing the already distributed cards 
    for i in range(0,4):       
        deck.pop(0)
    print(deck)
    print()
    print("Current Cards-")
    print (f'You: {player}')
    print(f'House: {house}')


    #asking user if they want to hit or not
def blackjack():
    ans = input("Do you want to hit?(y/n): ")
    p_sum = getSum(player)
    if ans == 'y' or ans == 'Y':
        while ans == 'Y' or ans == 'y' :       
            player_hit()
            p_sum = getSum(player)
            if p_sum >= 21:
                break
            ans = input("Do you want to hit?(y/n): ")

    if p_sum < 21:             
        h_sum = getSum(house)    
        while h_sum < 17:
            house.append(deck[0])
            deck.pop(0)
            print(f"House got {house[-1]}")
            print("Current Cards- ")
            print (f'You: {player}')
            print(f'House: {house}')
            h_sum = getSum(house)

    if p_sum > 21:
        print("House wins!")
    elif h_sum > 21:
        print("You win!")
    elif p_sum <= 21 and p_sum > h_sum:
        print("You win!")
    elif h_sum <= 21 and h_sum > p_sum:
        print("House Wins!")
    elif p_sum == h_sum and p_sum == 21:
        #TODO: Check who has black jack
        if has_blackjack(player):
            print("You Win!")
        elif has_blackjack(house):
            print("House Win!")
        else:
            print("No one wins.")
    else:
        print("No one wins.")

def player_hit():
    player.append(deck[0])
    deck.pop(0)
    print(f"You got {player[-1]}")
    print("Current Cards-")
    print (f'You: {player}')
    print(f'House: {house}')
    
def has_blackjack(deck):
    for i in range(0,len(deck)):
        if deck[i] == 'J\u2663':
            return True
    return False

deck = []
player = []
house = []
card_shuffle_and_dealing(deck,player,house)
blackjack()
