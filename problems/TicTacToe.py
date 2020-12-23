# 348. Design Tic-Tac-Toe
# #
# # Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
# #
# # A move is guaranteed to be valid and is placed on an empty block.
# # Once a winning condition is reached, no more moves are allowed.
# # A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# # Implement the TicTacToe class:
# #
# # TicTacToe(int n) Initializes the object the size of the board n.
# # int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
# # Follow up:
# # Could you do better than O(n2) per move() operation?
# #
# #
# #
# # Example 1:
# #
# # Input
# # ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
# # [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
# # Output
# # [null, 0, 0, 0, 0, 0, 0, 1]
# #
# # Explanation
# # TicTacToe ticTacToe = new TicTacToe(3);
# # Assume that player 1 is "X" and player 2 is "O" in the board.
# # ticTacToe.move(0, 0, 1); // return 0 (no one wins)
# # |X| | |
# # | | | |    // Player 1 makes a move at (0, 0).
# # | | | |
# #
# # ticTacToe.move(0, 2, 2); // return 0 (no one wins)
# # |X| |O|
# # | | | |    // Player 2 makes a move at (0, 2).
# # | | | |
# #
# # ticTacToe.move(2, 2, 1); // return 0 (no one wins)
# # |X| |O|
# # | | | |    // Player 1 makes a move at (2, 2).
# # | | |X|
# #
# # ticTacToe.move(1, 1, 2); // return 0 (no one wins)
# # |X| |O|
# # | |O| |    // Player 2 makes a move at (1, 1).
# # | | |X|
# #
# # ticTacToe.move(2, 0, 1); // return 0 (no one wins)
# # |X| |O|
# # | |O| |    // Player 1 makes a move at (2, 0).
# # |X| |X|
# #
# # ticTacToe.move(1, 0, 2); // return 0 (no one wins)
# # |X| |O|
# # |O|O| |    // Player 2 makes a move at (1, 0).
# # |X| |X|
# #
# # ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
# # |X| |O|
# # |O|O| |    // Player 1 makes a move at (2, 1).
# # |X|X|X|
# #
# #
# # Constraints:
# #
# # 2 <= n <= 100
# # player is 1 or 2.
# # 1 <= row, col <= n
# # (row, col) are unique for each different call to move.
# # At most n2 calls will be made to move.
from collections import defaultdict
# class TicTacToe(object):
#
#     def __init__(self, n):
#         """
#         Initialize your data structure here.
#         :type n: int
#         """
#         # We create a map of map for each row and each column and two diagonals
#         self.row_map=defaultdict(dict)
#         self.col_map=defaultdict(dict)
#         self.diag_map_top={}
#         for row in range(n):
#             for col in range(n):
#                 self.row_map[row][(row,col)]=-1
#                 self.col_map[col][(row,col)]=-1
#                 if row==col:
#                     self.diag_map_top[(row,col)]=-1
#         self.diag_map_bottom={}
#         for i in range(n):
#             self.diag_map_bottom[(n-i-1,i)]=-1
#
#
#     # Aim is to write move in less than O(n2) time
#     def move(self, row, col, player):
#         """
#         Player {player} makes a move at ({row}, {col}).
#         @param row The row of the board.
#         @param col The column of the board.
#         @param player The player, can be either 1 or 2.
#         @return The current winning condition, can be either:
#                 0: No one wins.
#                 1: Player 1 wins.
#                 2: Player 2 wins.
#         :type row: int
#         :type col: int
#         :type player: int
#         :rtype: int
#         """
#         def check_winner(map,player):
#             for value in map.values():
#                 if value!=player:
#                     return False
#             return True
#         # When we do a move we check for its diagonal,row,col if all have same values.If yes we have a winner
#         self.row_map[row][(row,col)]=player
#         is_winner=check_winner(self.row_map[row],player)
#         if is_winner:
#             return player
#         self.col_map[col][(row,col)]=player
#         is_winner=check_winner(self.col_map[col],player)
#         if is_winner:
#             return player
#         if (row,col) in self.diag_map_top:
#             self.diag_map_top[(row,col)]=player
#             is_winner=check_winner(self.diag_map_top,player)
#             if is_winner:
#                 return player
#         if (row,col) in self.diag_map_bottom:
#             self.diag_map_bottom[(row,col)]=player
#             is_winner=check_winner(self.diag_map_bottom,player)
#             if is_winner:
#                 return player
#         return 0
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        # We create a player map, for each player we define, row col and diag array.
        self.player_map=defaultdict(dict)
        for i in range(1,3):
            # Number of rows is equal to N, so is cols.Number of diagonal are 2 top down and botton up from right to left
            self.player_map[i]['row']=[0]*n
            self.player_map[i]['col']=[0]*n
            self.player_map[i]['diag']=[0]*2
        self.size=n



    # Aim is to write move in less than O(n2) time
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # We will increase each row/col/diagonal for the corresponding player and if any player reaches n, that is winner
        n=self.size
        # Fill and check each maps
        # So the corresponding index for a row is the count of elements in that row itself
        self.player_map[player]['row'][row]+=1
        if self.player_map[player]['row'][row]==n:
            return player
        self.player_map[player]['col'][col]+=1
        if self.player_map[player]['col'][col]==n:
            return player
        # For diag 1 i.e top diagonal
        if row==col:
            self.player_map[player]['diag'][0]+=1
            if self.player_map[player]['diag'][0]==n:
                return player
        # For diag 2 i.e bottom diagonal
        if n-col-1==row:
            self.player_map[player]['diag'][1]+=1
            if self.player_map[player]['diag'][1]==n:
                return player
        return 0




# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
# param_1 = obj.move(row,col,player)