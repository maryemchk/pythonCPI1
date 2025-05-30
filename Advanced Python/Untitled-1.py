def parser():
    while True:
        data = input().strip().split()
        for value in data:
            if value:
                yield value

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

def card_value(card):
    card_order = "23456789TJQKA"
    return card_order.index(card)

def play_war_games(games):
    results = []
    for i in range(0,len(games),2):
        player1_cards=games[i]
        player2_cards=games[i+1]
        while player1_cards and player2_cards:
            
            card1 = player1_cards.pop(0)
            card2 = player2_cards.pop(0)

            if card_value(card1) > card_value(card2):
                player1_cards.append(card2)
            elif card_value(card2) > card_value(card1):
                player2_cards.append( card1)
            else:
                player1_cards.append(card1)
                player2_cards.append(card2)
        print(player1_cards)
        print(player2_cards)
        



        if len(  player1_cards)==len( player2_cards):
            results.append("DRAW")
        elif  len(player2_cards)!=0:
            results.append("player 2")
        else:
            results.append("player 1")

    return results

# Read input
n = get_number()
games = []
for i in range(2*n):
    ls = input().strip().split()
    games.append(ls)

# Play the games and get results
results = play_war_games(games)

# Print results
for result in results:
    print(result)