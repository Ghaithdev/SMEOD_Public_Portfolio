class Game:
    def __init__(self, board, turn, players=None, pieces=None):
        self.board=board
        if not players:
            self.players=["White","Black"]
        else:
            self.players=players
        self.turn=players[turn]
        if not pieces:
            self.pieces=[]
        else:
            self.pieces=pieces
    
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
    
    def __init__(self, width, height, x_promotion=("all"), y_promotion=1, squares=None, letter_columns=True):
        if not squares:
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
        self.parent=parent
        self.x=x
        self.y=y
        self.contents=contents
        self.promotion=promotion
        self.name=self.get_name()
        self.coord=(x,y)
    
    def get_name(self):
        alphabet=list(map(chr, range(ord('a'), ord('z')+1)))
        if self.parent.letter_columns:
            x=alphabet[self.x]
        else:
            x=self.x
        coord=f"{x}{self.y}"
        return coord

class Piece():

    def __init__(self, type, colour, promotion=False, moves=None, location=None):
        self.type=type
        self.colour=colour
        self.promotion=promotion
        if not moves:
            self.moves=[]
        self.location=location
    
    def move(self, move):
        self.check_valid_move(move)
        pass

    def check_valid_move(move):
        

test=Board(5,5)
for square in test.squares:
    print(square,test.squares[square])