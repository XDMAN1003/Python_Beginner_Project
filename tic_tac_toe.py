import math
import random
import time

# Player class
class Player:
    def __init__(self,letter):
        #letter is X or O
        self.letter = letter

    #we want all players to get the next move goven a game
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):

    def __int__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __int__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter +"\'s turn . Input move (0-8):")
            # we are goinh to check this is a correct value by trying to cast
            # it to an integer and if it is not, then we say it is invalid
            # if that spot is not available on the board, we also say it is invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # If these are sucessful, then yay!
            except ValueError:
                print("Invalid square. Try again.")
        return val

class GeniusComputerPlayer(Player):
    def __int__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves) # random choice one
        else:
            # Get the square based off the minimax alogorithm
            square = self.minimax(game,self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                            state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


#  game class
class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game,x_player, o_player, print_game = True):
    #  returns the winner of the game (The letter of the winner)! or None for a tie
    if print_game:
        game.print_board_nums()
        print("")

    letter = "X"

    while game.empty_squares():
        # get the move form the appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #let's define a function to make a move
        if game.make_move(square,letter):
            if print_game:
                print(letter+f' make a move to square {square}')
                game.print_board()
                print("") #just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!\n')
                return letter

            #afrer we made our move we need to alternative letter
            letter = "O" if letter == "X" else "X" # switch player
            # if letter == "X":
            #    letter = "O"
            # else:
            # letter ="X"
        #tiny break
        time.sleep(0.8)

    if print_game:
            print("It is a tie game!\n")


if __name__ == '__main__':
    x_win = 0
    o_win = 0
    ties = 0
    index = 0
    for _ in range(5):
        print(f"\nRound {index}")
        x_player = RandomComputerPlayer("X")
        o_player = GeniusComputerPlayer("O")
        t = TicTacToe()
        result  = play(t,x_player,o_player,print_game=True)
        if(result == "X"):
            x_win +=1
        elif(result == "O"):
            o_win +=1
        else:
            ties += 1
        index+=1
    print(f"After 5 turns, {x_win} X wins, {o_win} O wins, {ties} ties. ")










