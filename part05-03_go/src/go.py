def who_won(game_board: list) -> int:
    player1, player2 = 0, 0
    
    for row in game_board:
        for element in row:
            if element == 1:
                player1 += 1
            elif element == 2:
                player2 += 1
                
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0
        
if __name__ == "__main__":
    board = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    print(who_won(board))