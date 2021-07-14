N = 8
row = [list()] * N #행
col = [list()] * N #열
inc = [list()] * (2*N-1) #오른쪽 위 대각선
dec = [list()] * (2*N-1) #오른쪽 아래 대각선

#piece = {}
value = {}

def locate(piece, cord):
    piece.cord = cord
    row[cord[0]].append(piece)
    col[cord[1]].append(piece)
    inc[cord[0] - cord[1] + N - 1].append(piece)
    dec[cord[0] + cord[1]].append(piece)

def inBoard(cord):
    return ( 0 <= cord[0] < N ) and ( 0 <= cord[1] < N )

class Pawn:
    cord = list()
    movble = list()
    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

        #find movable locations
        if inBoard([cord[0], cord[1] + 1]): self.movble.append([cord[0], cord[1] + 1])
        if inBoard([cord[0] - 1, cord[1] + 1]): self.movble.append([cord[0] - 1, cord[1] + 1])
        if inBoard([cord[0] + 1, cord[1] + 1]): self.movble.append([cord[0] + 1, cord[1] + 1])

class Rook:
    cord = list()
    movble = list()

    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

        # find movable locations
        for i in range(N):
            if i != cord[0]: self.movble.append([i, cord[1]])
            if i != cord[1]: self.movble.append([cord[0], i])

class Knight:
    cord = list()
    movble = list()

    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

        # find movable locations
        a, b = (1, 2)
        for i in range(2):
            a *= -1
            for j in range(2):
                b *= -1
                if inBoard([cord[0] + a, cord[1] + b]): self.movble.append([cord[0] + a, cord[1] + b])
                if inBoard([cord[0] + b, cord[1] + a]): self.movble.append([cord[0] + b, cord[1] + a])

class Bishop:
    cord = list()
    movble = list()

    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

        # find movable locations