class Game:
    def __init__(self, board, turn, players=None, pieces=None):
        self.board=Board(self, *board)
        if not players:
            self.players=["White","Black"]
        else:
            self.players=players
        self.turn=self.players[turn]
        if not pieces:
            self.pieces=[]
        else:
            self.pieces=pieces
    
    def set_pieces(self):
        for piece in Piece.inventory:
            print(piece.position,piece.type,piece.colour)

    
    def check_win(self):
        for player in self.players:
            if player.win_state=="Draw":
                self.game_end(state="Draw")
            if player.win_state==True:
                self.game_end(victor=player)
    
    def game_end(self, state="Victory", victor=None):
        if state=="Draw":
            pass
        else:
            print(victor)
            pass

class Board():
    
    def __init__(self, parent, width, height, x_promotion=("all"), y_promotion=1, letter_columns=True):
        self.game=parent
        self.squares={}
        self.width=width
        self.letter_columns=letter_columns
        self.height=height
        self.x_promotion=self.get_x_promotion(x_promotion)
        self.y1_promotion, self.y2_promotion=self.get_y_promotion(y_promotion)
        for x in range(self.width):
            for y in range(self.height):
                if x in self.x_promotion and y in self.y1_promotion:
                    promotion=1
                elif x in self.x_promotion and y in self.y2_promotion:
                    promotion=-1
                else:
                    promotion=0
                tile=Square(self,x,y, promotion=promotion)
                self.squares[tile.coord]={"name":tile.name,"square":tile}
        
    def get_x_promotion(self, x_promotion):
        output=[]
        if x_promotion=="all":
            for x in range(self.width):
                output.append(x)
        else:
            for coord in x_promotion:
                output.append(coord)
        return output
    
    def get_y_promotion(self, y_promotion):
        p1_output=[]
        p2_output=[]
        height=self.height-1
        for i in range(y_promotion):
            value=height-i
            if value not in p1_output and value>=0:
                p1_output.append(value)
            value=0+i
            if value not in p2_output and value<=height:
                p2_output.append(value)
        return p1_output, p2_output
            
class Square():

    def __init__(self,parent, x, y, contents=None, promotion=0):
        self.board=parent
        self.game=parent.game
        self.x=x
        self.y=y
        self.contents=contents
        self.promotion=promotion
        self.name=self.get_name()
        self.coord=(x,y)

    def get_name(self):
        alphabet=list(map(chr, range(ord('a'), ord('z')+1)))
        if self.board.letter_columns:
            x=alphabet[self.x]
        else:
            x=self.x
        coord=f"{x}{self.y}"
        return coord

class Piece():
    inventory=[]
    def __init__(self, colour,type, promotion=False, moves=None, start_pos=None):
        self.type=type
        self.colour=colour
        self.promotion=promotion
        if not moves:
            self.moves=[]
        self.s_position=start_pos
        Piece.inventory.append(self)
    
    def move(self, move):
        x=move[0]
        y=move[1]
        self.check_valid_move(x,y)
        pass

    def check_valid_move(self,x,y):
        if self.location[0]+x>self.parent.board.width:
            return False
        if self.location[1]+x>self.parent.board.height:
            return False
        if self.resolve_destination(x,y).contents:
            return False
        return True
    
    def check_promotion(self):
        if self.position in self.promotion:
            self.promote()
    
    def promote(self):
        print(f"Piece at {self.position} has promoted")
        

class Zensu_One_Piece(Piece):

    def __init__(self, starting_pos, colour):
        super.__init__(self, colour,"one",True,[(0,1),(2,0),(0,-3),(-4,0)], starting_pos)

class Zensu_Two_Piece(Piece):

    def __init__(self, starting_pos, colour):
        super.__init__(self, colour,"two",True,[(0,2),(3,0),(0,-4),(-1,0)], starting_pos)

test=Game((6, 10, "all", 1), 1)
class Zensu(Game):

    def __init__(self):
        p1_onesstart=[(0,1),(1,1),(2,1),(3,1),(4,1),(5,1)]
        p1_twosstart=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)]
        p2_onesstart=[(0,6),(1,6),(2,6),(3,6),(4,6),(5,6)]
        p2_twosstart=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7)]
        p1_pieces=[]
        p2_pieces=[]
        for pos in p1_onesstart:
            piece=Zensu_One_Piece("red",pos)
            p1_pieces.append(piece)
        for pos in p1_twosstart:
            piece=Zensu_Two_Piece("red",pos)
            p1_pieces.append(piece)
        for pos in p2_onesstart:
            piece=Zensu_One_Piece("green",pos)
            p1_pieces.append(piece)
        for pos in p2_twosstart:
            piece=Zensu_Two_Piece("green",pos)
            p1_pieces.append(piece)
    

zensu=Game((6, 10, "all", 1), 0, ["red","green"], [[one_piece,one_piece,one_piece,one_piece,one_piece,one_piece,two_piece,two_piece,two_piece,two_piece,two_piece,two_piece],[one_piece]])


for square in test.board.squares:
    print(square,test.board.squares[square]['square'].contents)
print(f"It is {test.turn}'s turn")