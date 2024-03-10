
player_1_msg = []
player_2_msg = []



while True:
    player_1 = input("Player1>>")
    player_1_msg.append(f'player 1: {player_1}')
    player_2 = input("Player2>>")
    player_2_msg.append(f'player 2: {player_2}')
    for x in player_1_msg:
        print(x)
        for y in player_2_msg:
            print(y)

