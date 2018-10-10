import numpy as np
class Board():
    def __init__(self):
        self.piece_names = ['empty','spy','scout',
                            'miner','sergeant','lieutenant',
                            'captain','major','colonel','general',
                            'marshal','flag','bomb','mountain']
        self.piece_map = {self.piece_names[i]:i for i in range(len(self.piece_names))}
        self.starting_piece_counts = {'spy':1,'scout':8,'miner':5,
                                      'sergeant':4,'lieutenant':4,'captain':4,
                                      'major':3,'colonel':2,'general':1,
                                      'marshal':1,'flag':1,'bomb':6}
        self.moveable_pieces = {i for i in range(1,11)}
        self.player1_piece_counts = {}
        self.player2_piece_counts = {}
        self.starting_pieces_per_player = 40
        self.board = [[0 for i in range(10)] for i in range(10)]
        self.add_mountains()
        self.player2_offset = 100
        self.player1_initialized = False
        self.player2_initialized = False
        self.player1_won = False
        self.player2_won = False
        self.player1_piece_positions = set()
        self.player2_piece_positions = set()

    def add_mountains(self):
        rows = [4,5]
        columns = [2,3,6,7]
        for row in rows:
            for column in columns:
                self.board[row][column] = self.piece_map['mountain']

    def add_player(self,pieces,player_number):
        assert player_number in [1,2]
        if player_number == 1 and self.player1_initialized:
            return False

        elif self.player2_initialized:
            return False

        if len(pieces) != self.starting_pieces_per_player:
            print(len(pieces))
            return False
        piece_counts = {}
        for piece in pieces:
            if piece <= 0 or piece >= len(self.piece_names) - 1:
                return False
            piece_name = self.piece_names[piece]
            if not piece_name in self.starting_piece_counts:
                return False
            if piece_name in piece_counts:
                curr_count = piece_counts[piece_name]
                if curr_count >= self.starting_piece_counts[piece_name]:
                    return False
                piece_counts[piece_name] += 1

        if player_number == 1:
            self.player1_piece_counts = piece_counts
            for j in range(10):
                for i in range(4):
                    piece_num = i * 10 + j
                    self.player1_piece_positions.add((i,j))
                    self.board[i][j] = pieces[piece_num]
            self.player1_initialized = True

        else:
            self.player2_piece_counts = piece_counts
            for j in range(10):
                for i in range(4):
                    piece_num = i * 10 + j
                    self.player2_piece_positions.add((9 - i,9 - j))
                    self.board[9 - i][9 - j] = pieces[piece_num] + self.player2_offset
            self.player2_initialized = True
        return True

    def attack(self,attacking,defending,player):
        assert player in [1,2]
        if player == 1:
            my_piece = attacking - self.player2_offset
            other_piece = defending
        else:
            my_piece = attacking
            other_piece = defending - self.player2_offset

        if other_piece == self.piece_map['bomb']:
            if my_piece == self.piece_map['miner']:
                return (attacking,defending)
            else:
                return (defending,attacking)
        elif other_piece == self.piece_map['flag']:
            if player == 1:
                self.player1_won = True
            else:
                self.player2_won = True
            return (attacking,defending)
        elif my_piece == self.piece_map['spy'] and other_piece == self.piece_map['marshal']:
            return (attacking,defending)
        else:
            if my_piece > other_piece:
                return (attacking,defending)
            elif other_piece > my_piece:
                return (defending,attacking)
            else:
                return (-1,-1)


    def move(self,start,end,player):
        if self.is_valid_move(start,end,player):
            my_piece = self.board[start[0]][start[1]]
            other_piece = self.board[end[0]][end[1]]
            self.board[start[0]][start[1]] = self.piece_map["empty"]
            if player == 1:
                self.player1_piece_positions.remove(start)
            else:
                self.player2_piece_positions.remove(start)
            if other_piece != self.piece_map["empty"]:
                winner,loser = self.attack(my_piece,other_piece,player)
                if (winner,loser) != (-1,-1):
                    self.board[end[0]][end[1]] = winner
                    if loser > self.player2_offset:
                        player2_piece_counts[self.piece_map[loser - self.player2_offset]] -= 1
                        if player == 1:
                            self.player2_piece_positions.remove(end)
                            self.player1_piece_positions.add(end)
                    else:
                        player1_piece_counts[self.piece_map[loser]] -= 1
                        if player == 2:
                            self.player1.piece_positions.remove(end)
                            self.player1.piece_positions.add(end)
                    return (my_piece,other_piece)
                else:
                    if player == 1:
                        self.player1_piece_positions.add(start)
                    else:
                        self.player2_piece_positions.add(start)
                    return (my_piece,other_piece)
            else:
                if player == 1:
                    self.player2_piece_positions.add(end)
                else:
                    self.player2_piece_positions.add(end)
                self.board[end[0]][end[1]] = my_piece
        else:
            return False

    def is_valid_scout_move_helper(self,start,end,player):
        assert player in [1,2]
        x1,y1 = start
        x2,y2 = end
        diff = x2-x1,y2-y1
        if diff[0] and diff[1]:
            return False
        elif diff[0]:
            for i in range(abs(diff[0])):
                if diff[0] < 0:
                    i = -i
                if (x1+i,y1) in self.player1_piece_positions or (x1+i,y1) in self.player2_piece_positions or self.piece_maps[(x1+i,y1)] == 'mountain':
                    return False
        else:
            for j in range(abs(diff[1])):
                if diff[1] < 0:
                    j = -j
                if (x1,y1+j) in self.player1_piece_positions or (x1,y1+j) in self.player2_piece_positions or self.piece_maps[(x1,y1+j)] == 'mountain':
                    return False
        #check the last tile
        if self.board[end[0]][end[1]] == 'mountain':
            return False
        if player == 1 and end in self.player1_piece_positions:
            return False
        elif end in self.player2_piece_positions:
            return False
        return True


    def is_valid_move(self,start,end,player):
        assert player in [1,2]
        if start == end:
            return False
        elif start[0] < 0 or start[0] > 9 or start[1] < 0 or start[1] > 9:
            return False

        elif end[0] < 0 or end[0] > 9 or end[1] < 0 or end[1] > 9:
            return False

        if self.board[end[0]][end[1]] == self.piece_map['mountain']:
            return False

        if player == 1:
            if end in self.player1_piece_positions:
                return False
            piece_num = self.board[start[0]][start[1]]
        else:
            if end in self.player2_piece_positions:
                return False
            piece_num = self.board[start[0]][start[1]] - self.player2_offset

        if not piece_num in self.moveable_pieces:
                return False

        if self.piece_names[piece_num] == 'scout':
            return self.is_valid_scout_move_helper(start,end,player)

        else:
            dirs = [(-1,0),(0,-1),(1,0),(0,1)]
            d1,d2 = end[0] - start[0], end[1] - start[1]
            for d in dirs:
                if d == (d1,d2):
                    return True
        return False

    def __repr__(self):
        return repr(np.array(self.board))

    def __str__(self):
        return str(np.array(self.board))
