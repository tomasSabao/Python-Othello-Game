from game import Game
def main(game_dimension):
    if (game_dimension < 2):
        game = Game(2)
    else:
        game = Game(game_dimension)
    game.draw_board()
    game.check_for_moves()
    

    while(game.is_game_over() == False):
        game.check_for_moves()
        ##if there are no moves to be made, switch turns
        if (game.can_player_act() == False):
            game.change_turn()
            continue
        game.show_current_player()
        game.show_hints()
        
        input = game.receive_input()
        if (game.input_is_valid(input) == True):
            game.set_piece(input)
            game.draw_board()
            game.print_score()
            game.change_turn()
    print("Game over. Thanks for playing")



main(3)

